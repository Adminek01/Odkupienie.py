import http.server
import socketserver
import logging
import os
import datetime
import subprocess
import base64
import platform
from Crypto.Cipher import AES

# HTTP server settings
HOST = '0.0.0.0'
PORT = 8080
LOGFILE = 'server.log'
INFECTED_FILES_DIR = 'infected_files'

# Encryption settings
ENCRYPTION_KEY = b'ThisIsASecretKey123'  # Use a stronger key and make it bytes
IV = os.urandom(16)

# Logging configuration
logging.basicConfig(filename=LOGFILE, level=logging.INFO)

# Custom HTTP request handler
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Your code to handle GET requests

# Create infected files directory if not exists
os.makedirs(INFECTED_FILES_DIR, exist_ok=True)

# Function to check if the target system is Windows
def is_windows():
    return platform.system() == 'Windows'

# Function to check if the tester's system is Kali Nethunter
def is_kali_nethunter():
    return platform.linux_distribution()[0] == 'Kali' and 'nethunter' in platform.version().lower()

# Check the tester's system
if not is_kali_nethunter():
    print("Warning: You are not using Kali Nethunter. Make sure you are testing with the correct system.")
else:
    # Execute remote command
    command = input("Enter a command to execute remotely: ")
    # Here you should implement the function to execute the command
    # execute_command(command)

# Start HTTP server
with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
    print(f'HTTP server is running on port {PORT}')
    httpd.serve_forever()
