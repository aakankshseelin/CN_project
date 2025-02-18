import socket
import ssl
import os

def send_file_to_server(filename, server_ip, server_port):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((server_ip, server_port)) as sock:
        with context.wrap_socket(sock, server_hostname=server_ip) as ssl_sock:
            with open(filename, 'rb') as f:
                file_data = f.read()
                ssl_sock.sendall(file_data)

if __name__ == '__main__':
    server_ip = '10.1.19.138'  # Server IP address (same as server)
    server_port = 8080       # Port number (same as server)

    while True:
        filename = input('Enter the filename to send (or type "exit" to quit): ')
        if filename.lower() == 'exit':
            break
        try:
            send_file_to_server(filename, server_ip, server_port)
            print(f'Successfully sent {filename} to the server.')
        except FileNotFoundError:
            print(f'File {filename} not found. Please try again.')

    print('Client connection terminated.')
