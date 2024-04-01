import socket


def start_client(host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))

        while True:
            message = input('Enter message: ')
            s.send(message.encode())
            if message == 'quit':
                break
            # message received from server
            data = s.recv(1024)
            print(f'Received from server: {data.decode()}')

        # close the connection
        s.close()


if __name__ == "__main__":
    start_client()
