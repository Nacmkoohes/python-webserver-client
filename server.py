import socket
import os

# server port
port=3823

# server root
server_root= os.path.abspath('.')
mime_types = {
    ".txt": "text/plain; charset=iso-8859-1",
    ".html": "text/html; charset=iso-8859-1",
    ".jpg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf"
}

def get_mime_type(file_name):
    _,ext= os.path.splitext(file_name)
    return mime_types.get(ext,"application/octet-stream")
def send_response(client_socket, status_code, content_type, content):
    response = f"HTTP/1.1 {status_code}\r\n"  # Correct initialization
    response += f"Content-Type: {content_type}\r\n"
    response += f"Content-Length: {len(content)}\r\n"
    response += "Connection: close\r\n\r\n"
    
    client_socket.send(response.encode() + content)

def send_404(client_socket):
    content = b"404 not found"
    send_response(client_socket, "404 Not Found", "text/plain; charset=iso-8859-1", content)
def handle_client(client_socket):
    try:
            request=client_socket.recv(1024).decode("ISO-8859-1")
            if not request:
                return
        #  header parsing
            request_lines = request.split("\r\n")
            first_line = request_lines[0].split()
            if len(first_line) < 2 or first_line[0] != "GET":
                send_404(client_socket)
                return
        # extracting file name
            requested_path = first_line[1]
            file_name = os.path.basename(requested_path)
            file_path = os.path.join(server_root, file_name)
        # preventing access to files outside the server
            if not file_name or ".." in requested_path or not os.path.abspath(file_path).startswith(server_root):
                send_404(client_socket)
                return
        # read and send file
            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as f:
                    content = f.read()
                    send_response(client_socket, "200 OK", get_mime_type(file_name), content)
            else:
                send_404(client_socket)
    finally:    
        client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)
    print(f"Server is running on port {port}...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    run_server()


