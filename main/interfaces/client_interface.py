from abc import ABC, abstractmethod

class ClientInterface(ABC):
    @abstractmethod
    def send_request(self, code_snippet):
        """
        Send a request to the server with a code snippet to be executed.
        """
        pass

    @abstractmethod
    def receive_response(self):
        """
        Receive a response from the server with the execution result.
        """
        pass

    @abstractmethod
    def handle_error(self, error):
        """
        Handle any errors that occur during the request/response process.
        """
        pass

    @abstractmethod
    def render_output(self, output):
        """
        Render the output from the server in the client view.
        """
        pass