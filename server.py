from fastapi import FastAPI
import uvicorn
import socket

app1 = FastAPI()


# Define routes for both servers
@app1.get("/")
def read_root_8080():
    return {"message": "Server 1 running on port 8080"}

# Function to get the IP address of the local machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Run both servers
def run_servers():
    # Get the IP address of the local machine
    ip_address = get_ip_address()

    # Print IP address and ports
    print(f"Server 1 running at http://{ip_address}:8080")

    # Launch both servers concurrently using Uvicorn
    config1 = uvicorn.Config(app1, host="0.0.0.0", port=8080, log_level="info")
    
    # Create separate servers for each app
    server1 = uvicorn.Server(config1)

if __name__ == "__main__":
    run_servers()






