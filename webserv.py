import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(1)
 
while 1:
    c, a = s.accept()
    data = c.recv(1024)
    splited = data.split(' ')
    f = open(splited[1], 'r')
    c.send("HTTP/1.1 200 OK \n" + f.read())
