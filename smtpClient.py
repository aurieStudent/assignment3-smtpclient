from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    clientSocket=socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))

    # Fill in end

    recv = clientSocket.recv(1024).decode()


    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()


    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom="Mail From: auriecat@gmail.com\r\n"
    clientSocket.send(mailFrom.encode())
    input=clientSocket.recv(1024).decode()

    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo=" RCPT: ac10984@nyu.edu\r\n"
    clientSocket.send(rcptTo.encode())
    input2=clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCo= "data\r\n"
    clientSocket.send(dataCo.encode())
    input3=clientSocket.recv(1024).decode()


    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    input4=clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCo="Quit\r\n"
    clientSocket.send(endmsg.encode())
    input5 = clientSocket.recv(1024).decode()
    clientSocket.close() #whoops lol forgot to close the socket
    # Fill in end
