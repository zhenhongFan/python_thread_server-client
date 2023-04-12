import socket
import threading
import time
IP = "172.24.49.41"
PORT = 8001

def recv_data(tcp_socket):
    while True:
        recv_data = tcp_socket.recv(1024)
        print("server: ",recv_data.decode("utf-8"))

def send_data(tcp_socket):
    while True:
        message = input()
        tcp_socket.send(message.encode("utf-8"))

def main():
    # 1 create
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2 connect server
    tcp_socket.connect((IP, PORT))
    
    # 3 send/receive
    recv_Thread = threading.Thread(target=recv_data, args=(tcp_socket,))
    send_Thread = threading.Thread(target=send_data, args=(tcp_socket,))
    recv_Thread.start()
    send_Thread.start()

    time.sleep(3000)
    # 4 close
    tcp_socket.close()
    
if __name__ == "__main__":
    main()