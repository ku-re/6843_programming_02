# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
      request_line = message.split('\r\n')[0]
      parts = request_line.split()
      filename = parts[1]
      if filename == "/":
        filename = "/helloworld.html"
      
      f = open("." + filename, "rb")    #fill in start              #fill in end   )
      filedata = f.read()
      f.close()

      #Fill in start 
      header = b"HTTP/1.1 200 OK\r\n"
      header += b"Content-Type: text/html; charset=UTF-8\r\n"
      header += b"Server: MyPythonServer\r\n"
      header += b"Connection: close\r\n"
      header += b"\r\n"
      #Fill in end
               
      for i in f: #for line in file
        pass #Fill in start - append your html file contents #Fill in end 
        
      # Fill in start
      connectionSocket.sendall(header + filedata)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      #Fill in start
      header = b"HTTP/1.1 404 Not Found\r\n"
      header += b"Content-Type: text/html; charset=UTF-8\r\n"
      header += b"Server: MyPythonServer\r\n"
      header += b"Connection: close\r\n"
      header += b"\r\n"
      body = b"<html><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.sendall(header + body)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

if __name__ == "__main__":
  webServer(13331)
