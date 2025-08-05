import qrcode
import os

def generate_qr():
    data = input("Enter text/URL to convert to QR code: ")
    filename = input("Enter filename (without extension): ")
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white") 
    python_folder_path = f"/Users/shammahuna/Documents/python files/{filename}.png"
    img.save(python_folder_path)
    
    print(f"QR code saved to: {python_folder_path}")


