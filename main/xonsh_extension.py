import os
from xonsh.environ import Env
from xonsh.aliases import Aliases

# Xonsh Shell Access
class Xonsh_Shell_Access:
    def __init__(self):
        self.env = Env(
            PATH=os.environ.get("PATH"),
            PWD=os.getcwd(),
            HOME=os.environ.get("HOME"),
            USER=os.environ.get("USER"),
            SHELL=os.environ.get("SHELL"),
        )
        self.aliases = Aliases()

    def execute(self, command):
        return self.aliases[command](self.env)

# Virtualized Access
class Virtualized_Access:
    def __init__(self, shell_access):
        self.shell_access = shell_access

    def execute(self, command):
        return self.shell_access.execute(command)

# File System Access
class File_System_Access:
    def __init__(self, shell_access):
        self.shell_access = shell_access

    def read(self, filepath):
        with open(filepath, 'r') as file:
            return file.read()

    def write(self, filepath, content):
        with open(filepath, 'w') as file:
            file.write(content)

    def execute(self, command):
        return self.shell_access.execute(command)

# Instantiate classes
xonsh_shell_access = Xonsh_Shell_Access()
virtualized_access = Virtualized_Access(xonsh_shell_access)
file_system_access = File_System_Access(xonsh_shell_access)