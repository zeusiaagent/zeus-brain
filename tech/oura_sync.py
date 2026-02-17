#!/usr/bin/env python3
import json
import requests
import os
from datetime import datetime, timedelta

OURA_TOKEN = open('tech/secrets/oura_token').read().strip()
SLEEP_URL = "https://api.ouraring.com/v2/usercollection/sleep"
DAILY_SLEEP_URL = "https://api.ouraring.com/v2/usercollection/daily_sleep"
DAILY_READINESS_URL = "https://api.ouraring.com/v2/usercollection/daily_readiness"
DATA_FILE = "data/saude.json"

headers = {"Authorization": f"Bearer {OURA_TOKEN}"}

try:
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    
    # Get sleep data (detailed metrics) - sleep from last night ends today
    sleep_resp = requests.get(f"{SLEEP_URL}?start_date={yesterday}&end_date={today}", headers=headers, timeout=10)
    sleep_data = sleep_resp.json().get('data', [])
    # Get sleep entry for today (the sleep that ended this morning)
    sleep_entry = next((s for s in sleep_data if s.get('day') == str(today)), sleep_data[0] if sleep_data else {})
    
    # Get daily sleep score (separate endpoint in v2)
    daily_sleep_resp = requests.get(f"{DAILY_SLEEP_URL}?start_date={today}&end_date={today}", headers=headers, timeout=5)
    daily_sleep_data = daily_sleep_resp.json().get('data', [])
    sleep_score = daily_sleep_data[0].get('score') if daily_sleep_data else None
    
    # Get daily readiness score
    readiness_entry = {}
    try:
        readiness_resp = requests.get(f"{DAILY_READINESS_URL}?start_date={today}&end_date={today}", headers=headers, timeout=5)
        readiness_data = readiness_resp.json().get('data', [])
        if readiness_data:
            readiness_entry = readiness_data[0]
    except:
        pass  # Readiness might not be available yet
    
    # Load or create saude.json
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            data = json.load(f)
    else:
        data = {"biomarkers": [], "suplementos": [], "sintomas": []}
    
    # Build entry
    entry = {
        "data": str(today),
        "sono_duracao": round(sleep_entry.get('total_sleep_duration', 0) / 3600, 1),
        "sono_qualidade": sleep_score,
        "sono_eficiencia": sleep_entry.get('efficiency', 0),
        "heart_rate": int(sleep_entry.get('average_heart_rate', 0)) if sleep_entry.get('average_heart_rate') else None,
        "hrv": int(sleep_entry.get('average_hrv', 0)) if sleep_entry.get('average_hrv') else None,
        "deep_sleep": round(sleep_entry.get('deep_sleep_duration', 0) / 3600, 1),
        "readiness": readiness_entry.get('score') if readiness_entry else None
    }
    
    # Update the data to match the format in the file
    new_data = {
        "sleep": f"{entry['sono_duracao']:.1f}h",
        "sleep_quality": entry['sono_qualidade'],
        "deep_sleep": f"{entry['deep_sleep']:.1f}h",
        "hr": entry['heart_rate'],
        "hrv": entry['hrv'],
        "readiness": f"{entry['readiness']}" if entry['readiness'] else "N/A"
    }
    
    # Save data
    with open(DATA_FILE, 'w') as f:
        json.dump(new_data, f, indent=2)
    
    # Print summary
    quality_str = f"{entry['sono_qualidade']}" if entry['sono_qualidade'] else "N/A"
    readiness_str = f"{entry['readiness']}" if entry['readiness'] else "N/A"
    hr_str = f"{entry['heart_rate']}" if entry['heart_rate'] else "N/A"
    hrv_str = f"{entry['hrv']}" if entry['hrv'] else "N/A"
    print(f"✅ Oura Updated: Sleep {entry['sono_duracao']:.1f}h (Quality {quality_str}, Deep {entry['deep_sleep']:.1f}h), HR {hr_str}, HRV {hrv_str}, Readiness {readiness_str}")

except Exception as e:
    print(f"❌ Oura API Error: {str(e)}")
