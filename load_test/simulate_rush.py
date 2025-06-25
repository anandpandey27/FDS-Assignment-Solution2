# load_test/simulate_rush.py
import requests, threading

def blast():
    requests.post("http://localhost:8000/request-charge")

threads = [threading.Thread(target=blast) for _ in range(100)]
[t.start() for t in threads]
[t.join() for t in threads]