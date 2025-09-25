import socket
import sys

def web_client(host,port=80):

    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode("ISO-8859-1"))
        response = b""
        while True:
            data = s.recv(8192)
            if not data:
                break
            response += data
    print(response.decode("ISO-8859-1"))
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python webclient.py <hostname> [port]")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    web_client(host, port)

