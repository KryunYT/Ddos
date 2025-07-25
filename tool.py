print("""
   _____       _ _     ___   __
  / ____|     | (_)   | \\ \\ / /
 | (___   ___ | |_  __| |\\ V / 
  \\___ \\ / _ \\| | |/ _` | > <  
  ____) | (_) | | | (_| |/ . \\ 
 |_____/ \\___/|_|_|\\__,_/_/ \\_\\
""")

import requests
import concurrent.futures

def send_request(url, i):
    try:
        response = requests.get(url)
        print(f"Request {i+1}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error sending request {i+1}: {e}")

def send_requests(url, count=10):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_request, url, i) for i in range(count)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    target = input("Enter the URL to send requests to (e.g., https://example.com): ")
    amount = input("Enter the number of requests (default is 10): ")
    try:
        count = int(amount)
    except:
        count = 10
    send_requests(target, count)
