import requests

url = "localhost:8080"
payload = {"lat": "49.5001611", "lon" : "8.4690878"}  # form fields
resp = requests.post(url, data=payload)

print("Status:", resp.status_code)
print("Response body:", resp.text)
