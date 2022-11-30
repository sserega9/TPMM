from socket import socket, AF_INET, SOCK_DGRAM


server_ip = '127.0.0.1'
server_port = 9001

buffer_size = 1024
encoding = 'utf-8'

message = 'Hello, world!'.encode(encoding)


def main() -> None:
    with socket(AF_INET, SOCK_DGRAM) as s:
        bytes_number = s.sendto(message, (server_ip, server_port))
        print(f'{bytes_number} bytes send to {server_ip}:{server_port}')

        received_message, addr = s.recvfrom(buffer_size)
        print(f'Received message from {addr[0]}:{addr[1]}')
        print(received_message.decode(encoding))

    print('Client socket is closed')


if __name__ == '__main__':
    main()
