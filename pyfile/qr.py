import qrcode

# URL to be encoded in the QR code
url = "http://127.0.0.1:8000/api/sessions/2"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code, try different values
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")