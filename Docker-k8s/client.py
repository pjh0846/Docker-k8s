#client.py
import os
import requests

def main():
    server_host = os.getenv('SERVER_HOST', 'localhost')
    server_port = os.getenv('SERVER_PORT', '8000')
    url = f"http://{server_host}:{server_port}"
    
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    main()
