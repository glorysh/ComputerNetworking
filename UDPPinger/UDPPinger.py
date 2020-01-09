from socket import *
import time

serverName = '10.0.8.35'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(0, 10):
    sendTime = time.time()
    message = ('Ping %d %s' % (i+1, sendTime)).encode()
    try:
        clientSocket.sendto(message, (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - sendTime
        print('Sequence %d: Reply from %s   RTT = %.3fs' % (i+1, serverName, rtt))
    except Exception as e:
        print('Sequence %d: Request time out' % (i+1))

clientSocket.close()