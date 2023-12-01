# /main.py
# =================xIMPORTS
import argparse
import asyncio
import datetime
import http.server
import json
import logging
import re
import socketserver
import sqlite3
import subprocess
import threading
import unittest
import requests
# import sub.modules in-line with their classes and functions

# ================xSERVER
PORT = 8080
server_main_url = 'http://localhost:{}'.format(PORT)

# =================xMAIN
from logs.test_ import *
from logs.exceptions_ import *
from logs.logging_ import *
e_=ErrorHandler_
l_=Logger_
def main():
    """
    This function acts as the primary entry point of the program:
    It parses command-line arguments, inits logging, runs unit tests, starts the static file server, and contains
    the core execution logic required to initialize and run the application.
    """
    #l_.debug()
    #l_.info()
    global Prompt__
    Prompt__ = Prompt__()
# ==================xSERVER
    def run_static_server():
        try:
            """Starts a static file server that can serve files and handle API requests on a specified port."""
            with socketserver.TCPServer("", PORT) as httpd:
                l_.info(f"Serving files and handling API requests on port {PORT}")
                httpd.serve_forever()
        except:
            l_.error(f"An error occurred.")
            sys.exit(1)
    try:
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        with socketserver.ThreadingTCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server")
        httpd.shutdown()
        httpd.server_close()
# ==================xTESTS
    test_suite = unittest.TestLoader().discover(start_dir='.', pattern='test_*.py')
    """
    Runs all the unit tests.
    """
    unittest.main()
    if result.wasSuccessful():
        l_.info("Tests passed successfully.")
        result = unittest.TextTestRunner().run(test_suite)
        threading.Thread(target=run_static_server).start()
    else:
        l_.error("Tests failed.")
        sys.exit(1)
# ================xARGS
    try:
        parser = argparse.ArgumentParser(description='COGNIC by MOONLAPSED@gmail.com MIT License')
        parser.add_argument('Prompt_', nargs='*', help='Enter the Prompt_ here')
        args = parser.parse_args()
        if not args.Prompt_:  # If the Prompt_ is empty, provide a default
            args.Prompt_.append('Hello world!')
        # Construct the Prompt_ as a single string
        Prompt_ = ' '.join(args.Prompt_).strip()  # Remove leading/trailing spaces
        l_.info(f"Prompt_: {Prompt_}")
        # API or other logic can be executed here
        # NOTE: This section will only execute if tests pass
        # Start the static file server
    except:
        e_.handle_error(sys.exc_info())
        l_.error("An error occurred.")

if __name__ == '__main__':
    try:
        main()
    except:
        e_.handle_error(sys.exc_info())
        l_.error("An error occurred.")