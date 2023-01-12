import requests

res = requests.get("https://api.ipify.org?format=json")
status_code = res.status_code
body = res.json()
print(status_code)
print(body)
