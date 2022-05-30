import socket

if __name__ == "__main__":
    # 1 创建客户端套接字对象, AF-INET表示IPv4地址类型，SOCK_STREAM表示TCP传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2 和服务端套接字建立连接
    tcp_client_socket.connect(("192.168.127.1", 8080))
    # 3 发送数据
    tcp_client_socket.send('nihaoma'.encode(encoding='utf-8'))
    # 4 接受数据 recv阻塞等待数据的到来
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode())
    # 5 关闭客户端套接字
    tcp_client_socket.close()