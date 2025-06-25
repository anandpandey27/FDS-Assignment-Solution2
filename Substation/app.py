from fastapi import FastAPI
from prometheus_client import Gauge, start_http_server
import random, time, threading

app = FastAPI()
load = Gauge("substation_current_load", "Active charging sessions")

@app.post("/charge")
def charge():
    load.inc()
    time.sleep(random.uniform(2, 5))
    load.dec()
    return {"message": "Charging complete"}

def serve_metrics():
    start_http_server(8001)

threading.Thread(target=serve_metrics).start()