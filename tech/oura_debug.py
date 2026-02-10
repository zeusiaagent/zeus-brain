#!/usr/bin/env python3
import json
import requests
from datetime import datetime, timedelta

OURA_TOKEN = open('tech/secrets/oura_token').read().strip()
OURA_URL = "https://api.ouraring.com/v2/usercollection/personal_info"
SLEEP_URL = "https://api.ouraring.com/v2/usercollection/sleep"
READINESS_URL = "https://api.ouraring.com/v2/usercollection/readiness"

headers = {"Authorization": f"Bearer {OURA_TOKEN}"}
today = datetime.now().date()
yesterday = today - timedelta(days=1)

try:
    # Debug: Get Readiness
    readiness_resp = requests.get(f"{READINESS_URL}?date={today}", headers=headers, timeout=10)
    print("READINESS RESPONSE:")
    print(json.dumps(readiness_resp.json(), indent=2))
    
    # Debug: Get Sleep
    sleep_resp = requests.get(f"{SLEEP_URL}?date={yesterday}", headers=headers, timeout=10)
    print("\nSLEEP RESPONSE:")
    print(json.dumps(sleep_resp.json(), indent=2))
    
except Exception as e:
    print(f"Error: {e}")
