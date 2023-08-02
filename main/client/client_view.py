import json
from client.client_model import ClientModel

class ClientView:
    def __init__(self):
        self.model = ClientModel()

    def render(self):
        output = self.model.get_output()
        errors = self.model.get_errors()

        if errors:
            print(f"Errors: {json.dumps(errors, indent=4)}")
        else:
            print(f"Output: {json.dumps(output, indent=4)}")

    def update_view(self, output, errors):
        self.model.set_output(output)
        self.model.set_errors(errors)
        self.render()