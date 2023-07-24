import os
from threading_core_utils import Threading_Core_Utils
from stdio_tasks import Stdio_Tasks
from unix_functionality import Unix_Functionality
from virtualized_access import Virtualized_Access

class File_System_Access:
    def __init__(self, path):
        self.path = path
        self.threading_core_utils = Threading_Core_Utils()
        self.stdio_tasks = Stdio_Tasks()
        self.unix_functionality = Unix_Functionality()
        self.virtualized_access = Virtualized_Access()

    def read_file(self, filename):
        with open(os.path.join(self.path, filename), 'r') as file:
            return file.read()

    def write_file(self, filename, content):
        with open(os.path.join(self.path, filename), 'w') as file:
            file.write(content)

    def execute_file(self, filename):
        self.unix_functionality.execute_command(os.path.join(self.path, filename))

    def list_files(self):
        return os.listdir(self.path)

    def change_directory(self, new_path):
        os.chdir(new_path)
        self.path = new_path

    def get_current_directory(self):
        return os.getcwd()

    def create_directory(self, dir_name):
        os.mkdir(os.path.join(self.path, dir_name))

    def delete_file(self, filename):
        os.remove(os.path.join(self.path, filename))

    def move_file(self, filename, new_path):
        os.rename(os.path.join(self.path, filename), os.path.join(new_path, filename))

    def copy_file(self, filename, new_path):
        self.unix_functionality.execute_command(f'cp {os.path.join(self.path, filename)} {new_path}')

    def get_file_permissions(self, filename):
        return self.unix_functionality.execute_command(f'ls -l {os.path.join(self.path, filename)}')

    def change_file_permissions(self, filename, permissions):
        self.unix_functionality.execute_command(f'chmod {permissions} {os.path.join(self.path, filename)}')

    def get_file_owner(self, filename):
        return self.unix_functionality.execute_command(f'ls -l {os.path.join(self.path, filename)}').split()[2]

    def change_file_owner(self, filename, new_owner):
        self.unix_functionality.execute_command(f'chown {new_owner} {os.path.join(self.path, filename)}')

    def get_file_group(self, filename):
        return self.unix_functionality.execute_command(f'ls -l {os.path.join(self.path, filename)}').split()[3]

    def change_file_group(self, filename, new_group):
        self.unix_functionality.execute_command(f'chgrp {new_group} {os.path.join(self.path, filename)}')