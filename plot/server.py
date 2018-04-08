import socket
import sys

# first of all, create a socket


def create_socket():
    try:
        global mysocket
        global port
        global host
        host = '192.168.8.2'
        port = 9999
        mysocket = socket.socket()
    except socket.error as msg:
        print(msg)


# bind server socket to a address
def bind_socket():
    try:
        global port
        global host
        global mysocket
        mysocket.bind((host, port))
        print('binding socket to port {}'.format(port))
        mysocket.listen(5)
    except socket.error as msg:
        print(msg, "retrying again...")
        bind_socket()


# accept clients
def socket_accept():
    try:
        global mysocket
        conn, address = mysocket.accept()
        print(
            "the connection has been established\naddress information: {}:{}".
            format(address[0], address[1]))
        send_result(conn)
        mysocket.close()
    except socket.error as msg:
        print(msg)


# after connection, send the message to client
def send_result(conn):
    while True:
        client_sent = conn.recv(1024).decode('utf-8')
        if len(client_sent) > 0:
            try:
                if client_sent == 'quit':
                    conn.close()
                    mysocket.close()
                    break
                number = float(client_sent)
                print('number', number)
                conn.send(str(number**2).encode('utf-8'))
            except Exception as e:
                print(e, client_sent)
                break
            

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
