"""
{
    "File": "hw13project2.py",
    "Author": "Daniel Egorov",
    "Date": "05/06/21",
    "Desc": [
        "client side of echo server"
    ],
    "Algorithm": [
        "establish connection",
        "send string to server",
        "receive and print the data sent back from server"
    ]
}

"""

# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# define hostname
host = '127.0.0.1'

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# get input from user and send to server
data = input()
s.send(data.encode('ascii'))                                     

# receive resulting string
res = s.recv(1024)

s.close()

print(res.decode('ascii'))
