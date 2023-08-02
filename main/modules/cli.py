import requests
from client.client_model import ClientModel
from client.client_view import ClientView
from client.client_controller import ClientController

class Client:
    def __init__(self, server_url):
        self.server_url = server_url
        self.model = ClientModel()
        self.view = ClientView()
        self.controller = ClientController(self.model, self.view)

    def send_code(self, code):
        response = requests.post(self.server_url, data={'code': code})
        if response.status_code == 200:
            self.model.update_model(response.json())
            self.controller.handle_input()
        else:
            print("Error: ", response.status_code)

    def start(self):
        while True:
            code = input("Enter Python code: ")
            self.send_code(code)

if __name__ == "__main__":
    client = Client("http://localhost:5000/execute")
    client.start()