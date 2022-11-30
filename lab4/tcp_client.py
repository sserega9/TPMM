from socket import socket, AF_INET, SOCK_STREAM


server_ip = '127.0.0.1'
server_port = 9000

encoding = 'utf-8'
buffer_size = 1024
message = 'Hello, world!'.encode(encoding)


def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        print('Connection with TCP server is opened')
        
        bytes_number = s.send(message)
        print(f'{bytes_number} bytes send to {server_ip}:{server_port}')

        received_message = s.recv(buffer_size).decode(encoding)
        print(f'Received message: {received_message}')

    print('Client socket is closed')


if __name__ == '__main__':
    main()
