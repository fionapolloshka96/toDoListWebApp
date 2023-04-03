FILE_PATH = "toDos.txt"


def get_todos(file_path=FILE_PATH):
    """ Returns a list of toDos inside the file."""
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, file_path=FILE_PATH):
    """ Writes a list of todos inside the text file."""
    with open(file_path, 'w') as file:
        file.writelines(todos)