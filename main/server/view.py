import json
from error_handling import handle_error

class View:
    def __init__(self):
        self.output = ""

    def render(self, data):
        try:
            self.output = json.dumps(data, indent=4)
        except Exception as e:
            handle_error(e)

    def get_output(self):
        return self.output

    def clear_output(self):
        self.output = ""