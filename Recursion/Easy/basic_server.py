import socket

def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        
        # Handle the client request
        handle_client(client_socket)
        
        # Close the client socket
        client_socket.close()

def handle_client(client_socket):
    # Define the HTML content as a string
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Server Example</title>
        </head>
            <body>
                <h1>Hello from the server!</h1>
                <p>This is a simple HTML page rendered by the server.</p>
            </body>
        </html>
    """
    
    # Prepare the HTTP response
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n\r\n"
        + html_content
    )
    
    # Send the HTTP response to the client
    client_socket.sendall(http_response.encode("utf-8"))

if __name__ == "__main__":
    server_host = "127.0.0.1"  # Use "0.0.0.0" to listen on all available network interfaces
    server_port = 8080
    start_server(server_host, server_port)
