import xonsh

class REPLModule:
    def __init__(self):
        self.repl = None

    def init_module(self):
        self.repl = xonsh.main.Xonsh()

    def execute_code(self, code):
        try:
            result = self.repl.execer.exec(code)
            return {'output': result, 'error': None}
        except Exception as e:
            return {'output': None, 'error': str(e)}

    def destroy_module(self):
        self.repl = None