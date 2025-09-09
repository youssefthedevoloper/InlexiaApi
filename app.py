from server import QRCodeServer

if __name__ == "__main__":
    server = QRCodeServer()
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
