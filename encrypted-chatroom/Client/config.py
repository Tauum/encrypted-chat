SERVER = input("Server IP ('' for default): ")
if SERVER.upper() == '':
    SERVER = '192.168.68.109'
    PORT = 9999
else:
    PORT = int(input("Server port: "))
ADDR = (SERVER, PORT)
HEADER = 64
FILE_CHUNK_SIZE = 16000  # bytes
DOWNLOADS_FOLDER_NAME = "downloads"
