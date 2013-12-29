'''
Created on Aug 28, 2013
'''
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
import socket

key = b'correcthorsebatterystaple'
nonce = b'incorrecthorse'
temp_key = SHA.new(key+nonce).digest()
cipher = ARC4.new(temp_key)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.1.1', 8081))
with open('nc', 'rb') as f:
	for line in f:
		sock.send(cipher.encrypt(line))
 
    
