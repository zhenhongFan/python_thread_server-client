import socket
import threading
import time
IP = "172.24.49.41"
PORT = 8001

def recv_data(new_client_socket):
    while True:
        recv_data = new_client_socket.recv(1024)
        if recv_data:
            print("client: ", recv_data.decode("utf-8"))
        else:
            break

def send_data(new_client_socket):
    while True:
        message = input()
        new_client_socket.send(message.encode("utf-8"))

def main():
    # create socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind ip and port
    tcp_server_socket.bind((IP, PORT))
    # listen
    tcp_server_socket.listen(128)

    while True:
        # wait client connect and accept
        print("wait client connect...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("%s has connected" % str(client_addr))

        # receive client message or send message to client
        recv_Thread = threading.Thread(target=recv_data, args=(new_client_socket,))
        send_Thread = threading.Thread(target=send_data, args=(new_client_socket,))
        recv_Thread.start()
        send_Thread.start()

        while True:
            if len(threading.enumerate()) <=2:
                break

        # close
        new_client_socket.close()
        print("loss connect...")
        time.sleep(1)
    tcp_server_socket.close()

if __name__ == "__main__":
    main()