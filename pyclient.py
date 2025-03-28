import socket

HOST = 'ip'
PORT = 12345
FILENAME = "example.txt"  # Replace with the file you want to send

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(FILENAME.encode())  # Send filename first
    
    with open(FILENAME, "rb") as file:
        while chunk := file.read(1024):
            client_socket.sendall(chunk)  # Send file data

print(f"File {FILENAME} sent successfully!")
