import socket

#  Make sure that the IP address and the port number for the
# client are the same as the server.
HOST = "127.0.0.1"
PORT = 5566

# We start by creating a TCP (Transmission Control Protocol) socket.
# The socket would be used to connect to the server and start
# communication.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is used for IPv4 and SOCK_STREAM is used for TCP
if client_socket is None:
    print("[-] Failed to create socket")
    exit(1)
else:
    print("[+] Created socket")

# We provide the required IP address and the port number to connect to the server.
# We send a connection request to the server and wait for the server to
# accept the request.
server_address = (HOST, PORT)
client_socket.connect(server_address)
print(f"[+] Connected to the server at {HOST}:{PORT}")

# Send data to the server
data = "HELLO, THIS IS CLIENT."
client_socket.send(data.encode()) # Send data to the socket. encode() converts the string to a bytes object.
print(f"Client: {data}")

# Receive data from the server
response = client_socket.recv(1024).decode() # Receive data from the socket. 1024 is the maximum amount of data to be received at once. decode() converts the bytes object to a string.
print(f"Server: {response}")

# Close the connection
client_socket.close()
print(f"[+] Disconnected from the server")
