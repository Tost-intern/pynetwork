import socket

HOST = '0.0.0.0'  
PORT = 12345       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()  
    with conn:
        print(f"Connected by {addr}")
        
        filename = conn.recv(1024).decode()  # Receive the filename
        print(f"Receiving file: {filename}")
        
        with open(f"received_{filename}", "wb") as file:
            while True:
                data = conn.recv(1024)  # Receive file data
                if not data:
                    break
                file.write(data)
        
        print(f"File {filename} received successfully!")
