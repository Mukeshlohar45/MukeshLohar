import requests
import json

url = "
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)

if response.status_code == 201:
    created_post = response.json()
    print("POST Response:")
    print(json.dumps(created_post, indent=2))
else:
    print(f"Error: {response.status_code}")"
getResponse = requests.get(url)

if getResponse.status_code == 200:
    fake_data = getRresponse.json()
    print("Fake Data:")
    print(json.dumps(fake_data, indent=2))
else:
    print(f"Error: {getResponse.status_code}")





