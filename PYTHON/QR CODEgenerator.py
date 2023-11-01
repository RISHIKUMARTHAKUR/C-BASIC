#QR code generator

from django import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qr.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black",black_color = "white")
    img.save("qrimg001.png")
    
generate_qrcode(https://www.linkedin.com/in/rishi-kumar-thakur-4a7235246/)