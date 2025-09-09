import numpy as np
import cv2
from .decoder import decode_qr_code

def handle_client(client_socket):
    try:
        print(f"Client connected: {client_socket.getpeername()}")
        size_data = b''
        while len(size_data) < 4:
            chunk = client_socket.recv(4 - len(size_data))
            if not chunk:
                return
            size_data += chunk
        frame_size = int.from_bytes(size_data, byteorder='big')
        print(f"Expecting frame size: {frame_size} bytes")
        frame_data = b''
        while len(frame_data) < frame_size:
            chunk = client_socket.recv(min(4096, frame_size - len(frame_data)))
            if not chunk:
                break
            frame_data += chunk
        if len(frame_data) == frame_size:
            nparr = np.frombuffer(frame_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if frame is not None:
                qr_texts = decode_qr_code(frame)
                if qr_texts:
                    response = "|".join(qr_texts).encode('utf-8')
                else:
                    response = b'NO_QR_DETECTED'
                response_size = len(response).to_bytes(4, byteorder='big')
                client_socket.send(response_size)
                client_socket.send(response)
                print(f"Sent response: {response.decode('utf-8')}")
            else:
                print("Failed to decode image")
                client_socket.send((0).to_bytes(4, byteorder='big'))
        else:
            print(f"Incomplete frame received: {len(frame_data)}/{frame_size}")
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
