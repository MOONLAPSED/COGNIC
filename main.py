# /main.py
# =================xIMPORTS
import argparse
import asyncio
import http.server
import re
import socketserver
import sqlite3
import subprocess
import threading
import requests
# import sub.modules in-line with their classes and functions

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
    try:
        # run_static_server()
        print(thisfails)
        print("Starting main()")
    except Exception as e:
        e_2 = sys.exc_info()[0]
        e_.handle_error(e)
        e_.handle_error(e_2)
        print("Ending main()", str(e_))
        sys.exit(1)

# ==================xSERVER
"""
def run_static_server():
    PORT = 8080
    server_main_url = 'http://localhost:{}'.format(PORT)
    try:
        #Starts a static file server that can serve files and handle API requests on a specified port.
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
    """

# ================xMAIN
if __name__ == "__main__":
    main()
