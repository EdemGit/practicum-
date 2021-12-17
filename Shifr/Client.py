import socket


def cript(msg, k):
    msgl = list(msg)
    for i in range(len(msgl)):
        msgl[i] = chr(ord(msgl[i]) + k)
    msg = ''.join(msgl)
    return msg


def decript(msg, k):
    msgl = list(msg)
    for i in range(len(msgl)):
        msgl[i] = chr(ord(msgl[i]) - k)
    msg = ''.join(msgl)
    return msg


    #Генерация ключа
def key_generation(ch1, n, Ksc): 
    Kpc = str(ch1 ** Ksc % n)
    return Kpc


def total_key_gen(Kps, Ksc, n):
    K = (Kps ** Ksc) % n
    return K



def main():
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect(('localhost', 9090))

    Ksc = int(input('Введите ключ из keys.csv):\n>'))

    data = sock.recv(1024).decode()
    data = data.split(' ')
    g = int(data[1])
    n = int(data[2])
    Kps = int(data[0])

    Kpc = key_generation(ch1, n, Ksc)
    print("Ключ сгенерирован")
    sock.send(Kpc.encode())

    K = total_key_gen(Kps, Ksc, n)
    print("Total key сгенерирован\n")

    data = sock.recv(1024).decode()
    data = decript(data, K)
    print(data)

    while True:
        msg = input()
        if msg == 'exit':
            break
        else:
            msg = cript(msg, K)

            sock.send(msg.encode())
        try:
            data = sock.recv(1024).decode()
        except:
            print("Стоп")
            break
        data = decript(data, K)
        print(data)

    sock.close()


main()
