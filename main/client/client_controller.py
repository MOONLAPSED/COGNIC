import requests
from client.client_model import ClientModel
from client.client_view import ClientView
from utils.fail_fast import fail_fast

class ClientController:
    def __init__(self):
        self.model = ClientModel()
        self.view = ClientView()

    def send_code_to_server(self, code):
        try:
            response = requests.post('http://localhost:5000/execute', data={'code': code})
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            fail_fast(f"HTTP error occurred: {err}")
        except Exception as err:
            fail_fast(f"An error occurred: {err}")
        else:
            return response.json()

    def update_model(self, response):
        self.model.update(response)

    def render_view(self):
        self.view.render(self.model)

    def handle_input(self, code):
        response = self.send_code_to_server(code)
        self.update_model(response)
        self.render_view()