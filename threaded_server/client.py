import socket
import threading


def post_data():
    while True:
        data = input()
        print()
        if data == 'quit':
            break
        client.send(f'{name}: {data}'.encode('utf-8'))
        print(f'{name}: {data}')


def get_data():
    while True:
        try:
            print(client.recv(1024).decode('utf-8'))
        except ConnectionAbortedError:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Enter required IP address: ')
name = input('Enter your name: ')

client.connect((host, 4603))
print('Connected to the server\nType \'quit\' to close the connection')

thread1 = threading.Thread(target=get_data, name='in')
thread2 = threading.Thread(target=post_data, name='out')

thread1.start()
thread2.start()

thread2.join()

print('Stopping')
client.close()
