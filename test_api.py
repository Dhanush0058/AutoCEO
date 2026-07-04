import urllib.request
import json

req = urllib.request.Request(
    'http://127.0.0.1:8000/api/orchestrator/query',
    data=b'{"query": "Check Runway"}',
    headers={'Content-Type': 'application/json'}
)

try:
    response = urllib.request.urlopen(req)
    print(json.dumps(json.loads(response.read()), indent=2))
except Exception as e:
    print(e)
