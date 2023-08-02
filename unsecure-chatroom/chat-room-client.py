import socket
import select
import sys
import server_details

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    # checks whether arguments have been provided
    server_details = server_details.get()
    print("no ip or port specified: python <script> IP-address port-number")
    print(f"defaulting for {server_details[0]} - {server_details[1]} - {server_details[2]}")

else:
    server_details = (str(sys.argv[1]), int(sys.argv[2]), socket.gethostname())

server.connect((server_details[1], server_details[2]))

while True:

    # maintains list of possible input streams
    sockets_list = [sys.stdin, server]

    """ Two possible input situations.
    select returns from sockets_list, the stream that is reader for input. """

    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        #  1. user wants to give manual input to send to other people,
        if socks == server:
            message = socks.recv(2048).decode()
            print(message)
        else:
            # 2. server is sending a message
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write("< You > ")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()