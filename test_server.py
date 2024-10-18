import subprocess
import requests
import time
import socket


# test root to ensure a good HTTP response and correct HTML page
def test_root_endpoint():

    # Start a server process we can test
    process = subprocess.Popen(["python", "server.py", "8080"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # The server might take a second to start
    time.sleep(1)
    
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        response = requests.get("http://" + ip_address + ":8080/")
        
        # The assert command throws an error if a False value is passed to it.
        assert response.status_code == 200
        print(response.content)

    # Terminate the server process after the test
    finally:
        process.terminate()

# test request endpoint to ensure a POST request is handled and a response is generated
def test_request_endpoint():

    # Start a server process we can test
    process = subprocess.Popen(["python", "server.py", "8080"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # The server might take a second to start
    time.sleep(1)
    
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        myobj = {'text' : 'test'}
        response = requests.post("http://" + ip_address + ":8080/request/", json=myobj)

        # The assert command throws an error if a False value is passed to it.
        print(response.text)
        assert response.status_code == 200

    # Terminate the server process after the test
    finally:
        process.terminate()
