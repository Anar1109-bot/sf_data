import socket

sock = socket.socket()

host = ("example.com", 80)

sock.connect(host)

request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n".encode()

sock.send(request)

data = sock.recv(4096)

print(data.decode("utf-8"))

sock.close()
