import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)
public_other = None
choice = input("host or join ?")

if choice == '1':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.68.109', 9999))
    server.listen()  # only handle 1 client
    client, _ = server.accept()  # when a client connects it will just accept (communication method)
    client.send(public_key.save_pkcs1('PEM'))
    public_other = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == '2':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.68.109', 9999)) # on another machine they would specify your public ip address
    public_other = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1('PEM'))

elif choice == '3':
    ipaddress = input("input ip")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipaddress, 9999))
    public_other = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1('PEM'))

else:
    exit()


def sending_message(c):
    while True:
        message = input("")
        c.send(rsa.encrypt(message.encode(), public_other))
        print(f"You: {message}")


def receiving_messages(c):
    while True:
        print(f"Other: {rsa.decrypt(c.recv(1024), private_key).decode()}")


threading.Thread(target=sending_message, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
