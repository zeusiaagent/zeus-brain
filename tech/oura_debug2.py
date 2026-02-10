#!/usr/bin/env python3
import json
import requests
from datetime import datetime, timedelta

OURA_TOKEN = open('tech/secrets/oura_token').read().strip()
READINESS_URL = "https://api.ouraring.com/v2/usercollection/readiness"

headers = {"Authorization": f"Bearer {OURA_TOKEN}"}
today = datetime.now().date()
yesterday = today - timedelta(days=1)

try:
    # Try with start_date and end_date params
    readiness_resp = requests.get(
        f"{READINESS_URL}?start_date={yesterday}&end_date={today}", 
        headers=headers, 
        timeout=10
    )
    print("READINESS WITH INTERVAL:")
    print(json.dumps(readiness_resp.json(), indent=2))
    
except Exception as e:
    print(f"Error: {e}")
