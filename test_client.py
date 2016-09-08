#test_client.py
import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'JSON',b'TOM',b'Micheal']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()