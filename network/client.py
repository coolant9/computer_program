# client.py

import socket
import sys

def main():
   # Create a socket object
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # Connect to the server
   host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
   port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
   client_socket.connect((host, port))
   print(f"Connected to server at {host}:{port}")

   message = "start"
   # Receive data from the server
   while message != "bye":
      data = client_socket.recv(1024)
      message = data.decode('utf-8')
      print(f"Received from server: {message}")

   # Close the connection
   client_socket.close()

if __name__ == "__main__":
    main()