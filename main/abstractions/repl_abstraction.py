from server.repl_server import execute_code
from server.error_handling import handle_error

class REPLAbstraction:
    def __init__(self):
        self.code_snippet = None
        self.execution_result = None

    def receive_code(self, code_snippet):
        self.code_snippet = code_snippet

    def execute_code(self):
        try:
            self.execution_result = execute_code(self.code_snippet)
        except Exception as e:
            handle_error(e)

    def get_execution_result(self):
        return self.execution_result

    def reset(self):
        self.code_snippet = None
        self.execution_result = None