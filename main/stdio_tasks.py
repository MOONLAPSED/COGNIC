import os
import subprocess
from threading import Thread

class Stdio_Tasks:
    def __init__(self, Server_Hardware_Access, Xonsh_Shell_Access):
        self.Server_Hardware_Access = Server_Hardware_Access
        self.Xonsh_Shell_Access = Xonsh_Shell_Access

    def execute_task(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout, stderr

    def execute_task_in_thread(self, command):
        thread = Thread(target=self.execute_task, args=(command,))
        thread.start()

    def get_file_content(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_to_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def append_to_file(self, file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)

    def delete_file(self, file_path):
        os.remove(file_path)

    def move_file(self, source_path, destination_path):
        os.rename(source_path, destination_path)

    def copy_file(self, source_path, destination_path):
        self.execute_task(f'cp {source_path} {destination_path}')

    def change_file_permissions(self, file_path, permissions):
        os.chmod(file_path, permissions)

    def execute_xonsh_command(self, command):
        return self.Xonsh_Shell_Access.execute_command(command)

    def get_server_hardware_info(self):
        return self.Server_Hardware_Access.get_hardware_info()