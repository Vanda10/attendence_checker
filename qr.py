import qrcode

# Function to generate QR code
def generate_qr_code(url, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(filename)

# Example usage
url = "https://attendence-checker-91c537c9caf5.herokuapp.com/sessions/2"
filename = "example_qr_code.png"
generate_qr_code(url, filename)
