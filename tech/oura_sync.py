#!/usr/bin/env python3
import json
import requests
import os
from datetime import datetime, timedelta

OURA_TOKEN = open('tech/secrets/oura_token').read().strip()
SLEEP_URL = "https://api.ouraring.com/v2/usercollection/sleep"
READINESS_URL = "https://api.ouraring.com/v2/usercollection/readiness"
DATA_FILE = "data/saude.json"

headers = {"Authorization": f"Bearer {OURA_TOKEN}"}

try:
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    
    # Get sleep from yesterday (noite anterior)
    sleep_resp = requests.get(f"{SLEEP_URL}?date={yesterday}", headers=headers, timeout=10)
    sleep_data = sleep_resp.json().get('data', [])
    sleep_entry = sleep_data[0] if sleep_data else {}
    
    # Try to get readiness (might be empty if not yet processed)
    readiness_entry = {}
    try:
        readiness_resp = requests.get(f"{READINESS_URL}?date={today}", headers=headers, timeout=5)
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
        "sono_duracao": sleep_entry.get('total_sleep_duration', 0) / 3600,
        "sono_qualidade": sleep_entry.get('sleep_score', 0),
        "sono_eficiencia": sleep_entry.get('efficiency', 0),
        "heart_rate": int(sleep_entry.get('average_heart_rate', 0)),
        "hrv": int(sleep_entry.get('average_hrv', 0)),
        "deep_sleep": sleep_entry.get('deep_sleep_duration', 0) / 3600,
        "readiness": readiness_entry.get('score') if readiness_entry else None
    }
    
    # Remove old entry for today if exists
    data['biomarkers'] = [b for b in data['biomarkers'] if b.get('data') != str(today)]
    data['biomarkers'].append(entry)
    
    # Keep only last 30 days
    if len(data['biomarkers']) > 30:
        data['biomarkers'] = data['biomarkers'][-30:]
    
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Print summary
    readiness_str = f"{entry['readiness']}" if entry['readiness'] else "N/A"
    print(f"✅ Oura Updated: Sleep {entry['sono_duracao']:.1f}h (Quality {entry['sono_qualidade']}, Deep {entry['deep_sleep']:.1f}h), HR {entry['heart_rate']}, HRV {entry['hrv']}, Readiness {readiness_str}")

except Exception as e:
    print(f"❌ Oura API Error: {str(e)}")
