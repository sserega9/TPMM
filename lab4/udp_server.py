from socket import socket, AF_INET, SOCK_DGRAM


ip = '127.0.0.1'
port = 9001

buffer_size = 1024
encoding = 'utf-8'


def main() -> None:
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((ip, port))
        print(f'UDP server is up on port {port}')

        while True:
            data, addr = s.recvfrom(buffer_size)
            if not data:
                break
            print(f'UDP server received message from {addr[0]}:{addr[1]}')
            print(f'Received message: {data.decode(encoding)}')
            bytes_number = s.sendto(data, addr)
            print(f'UDP server send {bytes_number} bytes to {addr[0]}:{addr[1]}')

    print('UDP server socket is closed')


if __name__ == '__main__':
    main()
