from client.client_model import ClientModel
from client.client_view import ClientView
from client.client_controller import ClientController
from utils.fail_fast import fail_fast

class ClientAbstraction:
    def __init__(self):
        self.model = ClientModel()
        self.view = ClientView()
        self.controller = ClientController(self.model, self.view)

    def send_code(self, code):
        try:
            response = self.controller.send_code(code)
            self.view.render(response)
        except Exception as e:
            fail_fast(str(e))

    def receive_output(self):
        try:
            output = self.controller.receive_output()
            self.view.render(output)
        except Exception as e:
            fail_fast(str(e))

    def update_view(self):
        try:
            self.view.update()
        except Exception as e:
            fail_fast(str(e))