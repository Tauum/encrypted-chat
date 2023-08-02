import socket
import threading

choice = input("host or join ?")

if choice == '1':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.68.109', 9999))
    server.listen()  # only handle 1 client
    client, _ = server.accept()  # when a client connects it will just accept (communication method)

elif choice == '2':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.68.109', 9999)) # on another machine they would specify your public ip address

elif choice == '3':
    ipaddress = input("input ip")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipaddress, 9999))

else:
    exit()


def sending_message(c):
    while True:
        message = input("")
        c.send(message.encode())
        print(f"You: {message}")


def receiving_messages(c):
    while True:
        print(f"Other: {c.recv(1024).decode()}")


threading.Thread(target=sending_message, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
