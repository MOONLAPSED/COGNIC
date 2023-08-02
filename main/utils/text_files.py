import os

def read_text_file(file_path):
    """
    Function to read a text file
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")

    with open(file_path, 'r') as file:
        return file.read()

def write_text_file(file_path, content):
    """
    Function to write to a text file
    """
    with open(file_path, 'w') as file:
        file.write(content)

def append_text_file(file_path, content):
    """
    Function to append to a text file
    """
    with open(file_path, 'a') as file:
        file.write(content)

def delete_text_file(file_path):
    """
    Function to delete a text file
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")

    os.remove(file_path)