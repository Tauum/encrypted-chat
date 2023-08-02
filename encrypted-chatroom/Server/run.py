from Server import Server
import socket
from prepare_server import run_prepare


run_prepare()
server = Server(socket.AF_INET, socket.SOCK_STREAM)
server.listen()
