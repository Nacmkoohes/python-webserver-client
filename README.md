# Python HTTP Server & Client

A minimal yet extended **client-server project** built with Python sockets.  
This repository demonstrates how HTTP requests and responses work at a low level and includes both a simple HTTP client/server and a more advanced file-serving HTTP server.

---

## Features

### Simple Web Server
- Listens on a TCP port (default: `28333`).
- Accepts raw socket connections.
- Parses incoming HTTP requests.
- Prints requests to the console for debugging and learning.

### Web Client
- Connects to a server and port.
- Sends a basic HTTP `GET /` request.
- Displays the server’s response in the console.

### Advanced HTTP File Server
- Custom HTTP server that serves static files (HTML, TXT, PNG, JPG, PDF).
- Implements **MIME type detection** and proper HTTP headers (Content-Type, Content-Length).
- Handles errors gracefully (e.g., `404 Not Found`).
- Demonstrates a practical extension of raw socket programming.

---

## Requirements
- Python 3.x  
(No third-party dependencies required)



