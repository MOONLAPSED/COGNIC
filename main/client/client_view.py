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
    
    def display_functions_and_methods(self):
        # This function should be implemented to display the available functions and class methods
        response = requests.get('http://localhost:5000/functions_and_methods')
        print("Available functions and class methods:", response.json())
    
    def select_function_or_method(self):
        # This function should be implemented to allow the user to select a function or method
        function_or_method = input("Please select a function or method: ")
        return function_or_method