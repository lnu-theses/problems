# load additional Python module
import socket, sys
from cryptography.fernet import Fernet


mode = sys.argv[1]

# create TCP/IP socket
sock = socket.socket()

port = 25002
print ('starting up on port ', port)
sock.bind(('localhost', port))

hardcoded_key = b'QcSn8bFgLgZMdZRWX84f9_GkeWCpnxWSnzCsTYj3PAQ='

sock.listen(1)

def decrypt_symmetric(data):
  f = Fernet(hardcoded_key)
  return f.decrypt(data)

def get_msg(data):
  if mode == "plain":
      return data
  elif mode == "sym":
      print("cipher text received, ", data)
      return decrypt_symmetric(data)


while True:
    # wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # show who connected to us
        print ('connection from', client_address)

        # receive the data in small chunks and print it
        while True:
            data = get_msg(connection.recv(512).decode())
            if data:
                # output received data
                print ("Data: ", data)
            else:
                # no more data -- quit the loop
                print ("no more data.")
                break

    finally:
        # Clean up the connection
        connection.close()

sock.close()
