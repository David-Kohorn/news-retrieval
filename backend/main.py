import requests

API_KEY = "773a9dc7cd75450d8c850256149561a6"
base_url = f"https://newsapi.org/v2/everything?q=Apple&from=2024-10-23&sortBy=popularity&apiKey={API_KEY}"
response = requests.get(base_url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Response Error {response.status_code}.")