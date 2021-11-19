import socket
import threading


def accept():
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f'Connected through {address}. {len(clients)} users connected.')


def receive(client):
    while True:
        try:
            data = client.recv(1024)
        except:
            clients.remove(client)
            end.remove(client)
            print(f'Server stopped. {len(clients)} users connected.')
            break
        print(data.decode('utf-8'))
        for client_ in clients:
            if client_ != client:
                client_.send(data)


def post_data():
    while True:
        data = input('Your message: ')
        if data == 'quit':
            break
        print(f'The \'{data}\' message sent to all clients')
        for client_ in clients:
            client_.send(data.encode('utf-8)'))


def get_data():
    while True:
        for client_ in clients:
            if client_ in end:
                continue
            index = threading.Thread(target=receive, args=(client_,))
            index.start()
            end.append(client_)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 4603))
server.listen(5)
print(f'Host: {socket.gethostname()}\nType \'quit\' to stop the server')
clients, end = [], []

t1 = threading.Thread(target=get_data, name='in')
t1.start()
t2 = threading.Thread(target=post_data, name='out')
t2.start()
t3 = threading.Thread(target=accept, name='accept')
t3.start()

t2.join()

for client_ in clients:
    client_.close()
print('Stopping')
