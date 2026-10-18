import requests
response = requests.get("https://api.github.com")

print(f"status code: {response.status_code}")
