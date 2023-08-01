import socket
import sys
from _thread import *
import server_details

"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    # checks whether arguments have been provided
    server_details = server_details.get()
    print("no ip or port specified: python <script> IP-address port-number")
    print(f"defaulting for {server_details[0]} - {server_details[1]} - {server_details[2]}")
else:
    # argument from command prompt as IP address and port
    server_details = (str(sys.argv[1]), int(sys.argv[2]), socket.gethostname())


# binds server to IP address and port number. Client MUST have these
print(f"defaulting for {server_details}")
server.bind((server_details[1], server_details[2]))
# the number of client available
server.listen(100)
list_of_clients = []


def client_thread(client, addr):
    # sends message to client whose user object is client
    client.send("Welcome to this unsecure-chatroom!".encode())
    while True:
            try:
                message = client.recv(2048).decode()
                if message:
                    # print message and address of user who sent message on server
                    print(f"< {addr[0]} > {message}")
                    # Calls broadcast function to send message to all
                    message_to_send = f"< {addr[0]} > {message}"
                    broadcast(message_to_send, client)
                else:
                    # message has no content or client is broken so remove it
                    remove_connection(client)
            except:
                continue


# broadcast message to all clients who is not the same as sending
def broadcast(message, client):
    for clients in list_of_clients:
        if clients != client:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                # if the link is broken, remove client
                remove_connection(clients)


def remove_connection(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:

    """Accepts connection requests and stores two parameters,
    client - socket object for that user
    addr - IP address of the client that"""
    client, addr = server.accept()

    # Maintains list for broadcasting message to all available clients
    list_of_clients.append(client)
    # prints address of the user just connected
    print(addr[0] + " connected")
    # creates individual thread for every user connected
    start_new_thread(client_thread, (client, addr))

conn.close()
server.close()
