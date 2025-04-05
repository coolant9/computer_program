# client.py

import socket

def main():
   # Create a socket object
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # Connect to the server
   host = 'tiger'
   port = 12345
   client_socket.connect((host, port))

   # Receive data from the server
   data = client_socket.recv(1024)
   print(f"Received from server: {data.decode('utf-8')}")

   # Close the connection
   client_socket.close()

if __name__ == "__main__":
    main()