import threading
import os
from xonsh.built_ins import XSH

class Threading_Core_Utils:
    def __init__(self, Server_Hardware_Access, Xonsh_Shell_Access, Virtualized_Access, File_System_Access, Unix_Functionality, Stdio_Tasks):
        self.Server_Hardware_Access = Server_Hardware_Access
        self.Xonsh_Shell_Access = Xonsh_Shell_Access
        self.Virtualized_Access = Virtualized_Access
        self.File_System_Access = File_System_Access
        self.Unix_Functionality = Unix_Functionality
        self.Stdio_Tasks = Stdio_Tasks

    def run_thread(self, target_function, *args):
        thread = threading.Thread(target=target_function, args=args)
        thread.start()
        return thread

    def run_shell_command(self, command):
        return self.Xonsh_Shell_Access.run(command)

    def access_file_system(self, path, mode):
        return self.File_System_Access.open(path, mode)

    def execute_unix_command(self, command):
        return self.Unix_Functionality.execute(command)

    def perform_stdio_task(self, task):
        return self.Stdio_Tasks.perform(task)

    def access_virtualized_system(self, command):
        return self.Virtualized_Access.execute(command)

    def access_server_hardware(self, command):
        return self.Server_Hardware_Access.execute(command)

if __name__ == "__main__":
    threading_core_utils = Threading_Core_Utils(XSH, XSH, XSH, os, os, os)
    threading_core_utils.run_thread(threading_core_utils.run_shell_command, "ls -l")