import json
import requests

url = 'http://35.230.13.35:8008/model'

request_data = json.dumps({'total_visits': 100, 'average_time_spent': 100})
response = requests.post(url, request_data)

print (response.text)
