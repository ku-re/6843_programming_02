# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  serverSocket.bind(("", port))
  
  serverSocket.listen(1)

  while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]

      f = open(filename[1:], "rb")
      filedata = f.read()
      f.close()

      header = b"HTTP/1.1 200 OK\r\n"
      header += b"Content-Type: text/html; charset=UTF-8\r\n"
      header += b"Server: MyPythonServer\r\n"
      header += b"Connection: close\r\n"
      header += b"\r\n"

      connectionSocket.sendall(header + filedata)
      connectionSocket.close()
      
    except Exception as e:
      header = b"HTTP/1.1 404 Not Found\r\n"
      header += b"Content-Type: text/html; charset=UTF-8\r\n"
      header += b"Server: MyPythonServer\r\n"
      header += b"Connection: close\r\n"
      header += b"\r\n"
      body = b"<html><body><h1>404 Not Found</h1></body></html>"

      connectionSocket.sendall(header + body)
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)
