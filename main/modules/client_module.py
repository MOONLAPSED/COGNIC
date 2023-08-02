import requests
from interfaces.client_interface import ClientInterface

class ClientModule:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client_interface = ClientInterface()

    def init_module(self):
        try:
            response = requests.get(self.server_url)
            if response.status_code == 200:
                print("Connected to the server successfully.")
            else:
                print("Failed to connect to the server.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def send_code(self, code):
        try:
            data = {"code": code}
            response = requests.post(self.server_url, json=data)
            if response.status_code == 200:
                return self.client_interface.receive_response(response.json())
            else:
                print("Failed to send the code to the server.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def destroy_module(self):
        self.server_url = None
        self.client_interface = None
        print("Client module destroyed.")