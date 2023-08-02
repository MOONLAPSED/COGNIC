class REPLExecutionError(Exception):
    """Exception raised for errors in the REPL execution.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class ClientServerError(Exception):
    """Exception raised for errors in the client-server interaction.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


def handle_error(error):
    """Function to handle errors and return structured data.

    Attributes:
        error -- error instance
    """
    error_data = {"type": type(error).__name__, "message": str(error)}
    return error_data