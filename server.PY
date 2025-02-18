import socket
import ssl
import threading

def handle_client(conn, fileno):
    try:
        filename = f'output{fileno}.txt'
        with open(filename, "wb") as fo:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                fo.write(data)
        print(f'Received file from client {fileno}: {filename}')
    finally:
        conn.close()

if __name__ == '__main__':
    host = '10.1.19.138'  # Server IP address (localhost for testing)
    port = 8080            # Port number

    total_clients = int(input('Enter the number of clients: '))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('file.crt', 'file.key')

    ssl_sock = context.wrap_socket(sock, server_side=True)
    ssl_sock.bind((host, port))
    ssl_sock.listen(total_clients)

    connections = []
    print('Initiating clients...')
    try:
        for i in range(total_clients):
            conn, _ = ssl_sock.accept()
            connections.append(conn)
            print(f'Connected with client {i + 1}')
            threading.Thread(target=handle_client, args=(conn, i + 1)).start()
    finally:
        ssl_sock.close()

    print('All files received successfully!')
