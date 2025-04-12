# server.py
import socket
def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = 'localhost'
    port = 12345

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        message = 'Thank you for connecting'
        client_socket.send(message.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    main()