'''
Created on Aug 28, 2013
'''

from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
import socket

key = b'correcthorsebatterystaple'
nonce = b'incorrecthorse'
temp_key = SHA.new(key+nonce).digest()
cipher = ARC4.new(temp_key)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 8081))
sock.listen(5)

conn, addr = sock.accept()

with open('workfile', 'wb') as f:

	while 1:
		data = conn.recv(1024)
		if not data: 
			break
		f.write(cipher.decrypt(data))

    

'''
with open('workfile', 'rb') as f:
    message = f.read()



print cipher.decrypt(message)
'''
