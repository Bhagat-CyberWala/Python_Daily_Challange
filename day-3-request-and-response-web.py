import socket
target=input("Enter your target domain name : ")
port=80

#ccreate a socket object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to client
client.connect((target,port))

#send data
client.send(b"GET / HTTP/1.1\r\nhost:{target}\r\n\r\n")

#response 
response=client.recv(10000)
print(response.decode())

client.close()
