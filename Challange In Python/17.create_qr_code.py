import qrcode
from random import random

def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    rand = random()
    img.save(f"pyqrimg{rand}.png")

url = input("Enter Your Url")
generate_qr_code(url)