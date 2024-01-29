import socket, sys
from cryptography.fernet import Fernet

mode = sys.argv[1]

hardcoded_key = b'QcSn8bFgLgZMdZRWX84f9_GkeWCpnxWSnzCsTYj3PAQ='


def encrypt_symmetric(data):
  f = Fernet(hardcoded_key)
  encrypted = f.encrypt(data)
  print("cipher text ", encrypted)
  return encrypted

def get_msg(data):
  if mode == "plain":
      return data
  elif mode == "sym":
      return encrypt_symmetric(data)

client_socket = socket.socket()
port = 25002
client_socket.connect(('localhost', port))
while True:
    data = input("input msg (q to quit):")
    client_socket.sendall(get_msg(data.encode("utf-8")))
    if data.lower() == 'q':
        client_socket.close()
        break
