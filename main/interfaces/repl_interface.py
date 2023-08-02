from abc import ABC, abstractmethod

class REPLInterface(ABC):
    @abstractmethod
    def execute_code(self, code: str):
        """
        Execute the given code snippet on the server.
        """
        pass

    @abstractmethod
    def start_server(self):
        """
        Start the Xonsh Python REPL server.
        """
        pass

    @abstractmethod
    def stop_server(self):
        """
        Stop the Xonsh Python REPL server.
        """
        pass

    @abstractmethod
    def send_request(self, request: dict):
        """
        Send a request to the server.
        """
        pass

    @abstractmethod
    def receive_response(self):
        """
        Receive a response from the server.
        """
        pass