import requests


url = f"http://localhost:8080?lat=49.5000297&lon=8.4690313&timestamp=1775585542411&hdop=9.935046&altitude=160.82843&speed=0.0"
resp = requests.post(url)

print("Status:", resp.status_code)
print("Response body:", resp.text)
