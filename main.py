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

def main():
    data = input("Enter the URL to encode: ")
    color = input("Choose a color: ")

    qr_img = create_qr(data, color)
    qr_img.show()

if __name__ == "__main__":
    main()
