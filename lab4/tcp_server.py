from socket import socket, AF_INET, SOCK_STREAM


ip = '127.0.0.1'
port = 9000

buffer_size = 1024
encoding = 'utf-8'


def main() -> None:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()
        print(f'TCP server is listening on port {port}')

        while True:
            conn, addr = s.accept()
            print(f'TCP server accepted connection from {addr[0]}:{addr[1]}')
            with conn:
                while True:
                    data = conn.recv(buffer_size)
                    if not data:
                        break
                    print(f'TCP server received message: {data.decode(encoding)}')
                    bytes_number = conn.send(data)
                    print(f'TCP server send {bytes_number} bytes to {addr[0]}:{addr[1]}')


if __name__ == '__main__':
    main()
