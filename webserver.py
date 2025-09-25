lsimport socket
import sys

def web_server(port=28333):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# Allow the port to be reused after the server terminates
        s.bind(("", port))
        s.listen()
        print(f"Server listening on port {port}...")

        while True:
            conn, addr = s.accept()  #Accept a new connection
            with conn:
                print(f"Connected by {addr}")
                request = b""

                while True:
                    data = conn.recv(1024)
                    request += data
                    if not data or b"\r\n\r\n" in request:
                        break
                    
                print(f"Received request: {request.decode('ISO-8859-1')}")

                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Type: text/plain\r\n\r\n"
                response += "Content-Length: 6\r\n"
                response += "Connection: close\r\n\r\n"
                response += "Hello!"
                
                
                conn.sendall(response.encode("ISO-8859-1"))
                print("Response sent, closing connection")

                

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 28333
    web_server(port)