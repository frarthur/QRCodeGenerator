import qrcode
from PIL import Image

def create_qr(data, color='black'):
    # Simple QR code
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Color 
    qr_img = qr.make_image(fill_color=color, back_color="white")
    qr_img = qr_img.convert("RGB")

    return qr_img

def add_logo(qr_img, center_img_path):
    qr_width, qr_height = qr_img.size
    center_img = Image.open(center_img_path)
    
    # Resize the logo
    factor = 4  # You can change this var to resize the logo
    size_w = qr_width // factor
    size_h = qr_height // factor
    center_img = center_img.resize((size_w, size_h), Image.Resampling.LANCZOS)
    
    # Calcul pos
    pos = ((qr_width - size_w) // 2, (qr_height - size_h) // 2)
    
    # Paste logo on the QRCode
    qr_img.paste(center_img, pos, center_img)
    return qr_img

def main():
    data = input("Enter the URL to encode: ")
    color = input("Choose a color: ")
    center_img_path = input("Enter path to the logo (optional): ")

    qr_img = create_qr(data, color)

    if center_img_path:
        qr_img = add_logo(qr_img, center_img_path)
    
    qr_img.show()

if __name__ == "__main__":
    main()
