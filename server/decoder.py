import cv2
import pyzbar.pyzbar as pyzbar

def decode_qr_code(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_objects = pyzbar.decode(gray)
    results = []
    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        results.append(qr_data)
        print(f"QR Code detected: {qr_data}")
    return results
