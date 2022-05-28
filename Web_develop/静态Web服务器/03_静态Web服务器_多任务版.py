import socket
import threading

def handle_client_request(client_socket):        # 获取浏览器的请求信息
    client_request_data = client_socket.recv(1024).decode()
    # print(client_request_data)
    # 获取用户请求资源的路径
    request_data = client_request_data.split(' ')
    if len(request_data) == 1:
        client_socket.close()
        return
    request_path = request_data[1]
    if request_path == "/":
        request_path = "/index.html"

    # 3. 读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
    try:
        with open('.\Python\Web_develop\静态Web服务器'+ request_path, 'rb') as f:
            file_data = f.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_header = "Server: pwb\r\n"
        response_body = "404 Not Found Sorry"
        response_data = (response_line + response_header + "\r\n" + response_body).encode('utf-8')
        client_socket.send(response_data)
        pass
    else:
        # 应答行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 应答头
        response_header = "Server: pwb\r\n"
        # 应答体
        response_body = file_data
        response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        client_socket.send(response_data)
    finally:
        # 4. HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字
        client_socket.close()


if __name__ == '__main__':
    # 1. 编写一个TCP服务端程序
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定地址及端口
    tcp_server_socket.bind(('', 8080))
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 2. 获取浏览器发送的HTTP请求报文数据
        # 建立连接
        client_socket, client_addr = tcp_server_socket.accept()
        # 创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(client_socket,))
        sub_thread.start()

