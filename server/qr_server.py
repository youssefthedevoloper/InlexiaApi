import socket
import threading
from .handlers import handle_client

class QRCodeServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            print(f"QR Code Server started on {self.host}:{self.port}")
            print("Waiting for ESP32-CAM connections...")
            while self.running:
                try:
                    client_socket, addr = self.server_socket.accept()
                    client_thread = threading.Thread(
                        target=handle_client,
                        args=(client_socket,)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                except KeyboardInterrupt:
                    print("Server shutting down...")
                    break
                except Exception as e:
                    print(f"Error accepting connection: {e}")
        except Exception as e:
            print(f"Failed to start server: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()

    def stop_server(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
