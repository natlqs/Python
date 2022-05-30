import socket

if __name__ == '__main__':
    # 1 创建服务端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2 绑定IP地址和端口号,如果bind中的参数第一个IP地址元素设置为""，默认为本机IP地址
    tcp_server_socket.bind(("192.168.127.1", 8080))
    # 3 设置监听 128:代表服务端等待排队连接的最大数量
    tcp_server_socket.listen(128)
    # 4 等待接受客户端的连接请求   accept阻塞等待  返回一个用以和客户端通讯的socket，客户端的地址
    conn_socket, ip_port = tcp_server_socket.accept()
    print("客户端地址：", ip_port)
    # 5 接收数据
    recv_data = conn_socket.recv(1024)
    print("接收到的数据：", recv_data.decode('utf-8'))
    # 6 发送数据
    conn_socket.send("客户端你的数据我收到了".encode())
    # 7 关闭套接字
    conn_socket.close()
    tcp_server_socket.close()