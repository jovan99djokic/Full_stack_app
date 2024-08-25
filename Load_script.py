import requests
import random
import json
from concurrent.futures import ThreadPoolExecutor

# Endpoint URL
url = 'http://127.0.0.1:5000/create_contact'

# Random data
first_names = ["Petar", "Marko", "Ivan", "Nikola", "Stefan"]
last_names = ["Petrovic", "Markovic", "Ivanovic", "Nikolic", "Stefanovic"]
domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]

# Number of requests to send
num_requests = 25
# Number of concurrent threads
num_threads = 5

def generate_random_data():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
    return {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }

def send_post_request():
    try:
        data = generate_random_data()
        headers = {
            "Content-Type": "application/json",
            "sec-ch-ua": '"Chromium";v="127", "Not)A;Brand";v="99"',
            "Accept-Language": "en-US",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
            "sec-ch-ua-platform": '"Linux"',
            "Accept": "*/*",
            "Origin": "http://my-app.test:5173",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "http://my-app.test:5173/",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"Sent data: {data} | Response Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def load_test():
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(num_requests):
            executor.submit(send_post_request)

if __name__ == "__main__":
    load_test()
