from fastapi import FastAPI
import os, requests, re

app = FastAPI()
SUBSTATIONS = os.getenv("SUBSTATION_URLS").split(",")

@app.post("/route")
def route():
    loads = {}
    for url in SUBSTATIONS:
        try:
            r = requests.get(f"{url}/metrics")
            match = re.search(r'substation_current_load (\d+)', r.text)
            if match:
                loads[url] = int(match.group(1))
        except:
            loads[url] = float("inf")
    best = min(loads, key=loads.get)
    return requests.post(f"{best}/charge").json()