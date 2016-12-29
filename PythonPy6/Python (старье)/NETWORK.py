import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80)) #connect through port

mysock.send('http://py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode()) #command of GET to server+encode

while True:
    data=mysock.recv(512).decode() #print:)
    if (len(data)<1): break
    print (data)
mysock.close()

#Using urllib
import urllib.request as ur
handle=ur.urlopen.encode()('http://py4inf.com/code/mbox-short.txt')
for line in handle:
    line=line.rstrip()

