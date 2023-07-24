import os
from xonsh.built_ins import run

class VirtualizedAccess:
    def __init__(self):
        self.shell_access = Xonsh_Shell_Access()
        self.file_system_access = File_System_Access()

    def run_command(self, command):
        return self.shell_access.run_command(command)

    def read_file(self, filepath):
        return self.file_system_access.read_file(filepath)

    def write_file(self, filepath, content):
        self.file_system_access.write_file(filepath, content)

class Xonsh_Shell_Access:
    def run_command(self, command):
        return run(command)

class File_System_Access:
    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            return file.read()

    def write_file(self, filepath, content):
        with open(filepath, 'w') as file:
            file.write(content)

if __name__ == "__main__":
    virtualized_access = VirtualizedAccess()
    print(virtualized_access.run_command('ls'))
    print(virtualized_access.read_file('llama_model.py'))
    virtualized_access.write_file('test.txt', 'Hello, World!')