import socket
import time
import threading

def handle_client(conn, addr):
    print "Connection from {}".format(addr)
    start_time = time.time()
    total_received = 0
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            total_received += len(data)
    finally:
        end_time = time.time()
        conn.close()
        print "Data received: {} bytes".format(total_received)
        print "Time taken: {} seconds".format(end_time - start_time)
        print "Bandwidth: {:.2f} MB/s".format(total_received / (end_time - start_time) / (1024*1024))

def server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print "Listening for connections on {}:{}".format(host, port)

    try:
        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
    finally:
        server_socket.close()

if __name__ == "__main__":
    server()
