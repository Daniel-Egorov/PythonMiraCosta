"""
{
    "File": "hw13project2.py",
    "Author": "Daniel Egorov",
    "Date": "05/06/21",
    "Desc": [
        "server side of echo server"
    ],
    "Algorithm": [
        "establish server",
        "receive string from client",
        "reverse the string and send back to client"
    ]
}

"""

import socket                                         
import time

# create a socket object
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# define hostname
host = '127.0.0.1'

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))

    # receive string from client
    data = clientsocket.recv(1024)
    data = data[::-1]
    clientsocket.send(data)

    clientsocket.close()