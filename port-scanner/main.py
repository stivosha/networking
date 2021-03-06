import multiprocessing
import socket
import sys


def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((ip, port))
            print(f'TCP PORT : {port} is open.')
            sock.close()
        except:
            pass


def tcp_scan(ip, startPort, endPort):
    print(f'Start scanning for tcp ports of {ip}')
    res = []
    for port in range(startPort, endPort + 1):
        new_connection = multiprocessing.Process(target=scan_port, args=(ip, port))
        res.append(new_connection)
        new_connection.start()
    for connect in res:
        connect.join()


if __name__ == '__main__':
    ip, startPort, endPort = sys.argv[1], int(sys.argv[2]),  int(sys.argv[3])
    tcp_scan(ip, startPort, endPort)
