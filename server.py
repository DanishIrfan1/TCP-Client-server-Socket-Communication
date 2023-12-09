import socket  # For socket creation and manipulation

# Define the IP (Internet Protocol) address and port number, that would
# be used to create a socket. Here, we are using the localhost address for
# both the server and the client. The port number is 5566.
HOST = "127.0.0.1"
PORT = 5566

# Create a TCP (Transmission Control Protocol) socket that returns a
# socket descriptor. This socket descriptor would be used to
# communicate with the client.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is used for IPv4 and SOCK_STREAM is used for TCP
if server_socket is None:
    print("[-] Failed to create socket")
    exit(1)
else:
    print("[+] Created socket")

# Here, we initialize the server address by providing the required IP and
# port number.Binding the socket descriptor with the server address information.
server_address = (HOST, PORT)
server_socket.bind(server_address) # Bind the socket to the server address

if server_socket is None:
    print("[-] Failed to bind socket")
    exit(1)
else:
    print(f"[+] Bound socket to {HOST}:{PORT}")

# Now, we listen for incoming connections from the clients.
server_socket.listen(5) # listen for connections made to the socket. The argument specifies the maximum number of queued connections.
print(f"[+] Listening for connections on {HOST}:{PORT}")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept() # Accept a connection. The socket must be bound to an address and listening for connections.
    print(f"[+] Client connected from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode() # Receive data from the socket. 1024 is the maximum amount of data to be received at once. decode() converts the bytes object to a string.
    print(f"Client: {data}")

    # Send data back to the client
    response = "HI, THIS IS SERVER. HAVE A NICE DAY!!!"
    client_socket.send(response.encode()) # Send data to the socket. encode() converts the string to a bytes object.
    print(f"Server: {response}")

    # Close the connection
    client_socket.close()
    print(f"[+] Client disconnected")

    break # Remove this line to allow multiple clients to connect
# Close the server socket
server_socket.close()
print("[+] Server closed")
