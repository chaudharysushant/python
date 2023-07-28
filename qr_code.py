import qr_code

def qr_code_generator(data, filename):
    qr = qr_code.QRCode(
        version = 1,
        error_correction = qr_code.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 5
    )

    qr_code.add_data(data)
    qr_code.make(fit=True)

    img=qr_code.make_image(fill_color ="black", back_color = "white")
    img.save(filename)

if __name__ == "__main__":
    data_to_encode = "QR CODE GENERATOR!"
    qr_code_filename = "qr_img.jpg"

    generate_qr_code = (data_to_encode, qr_code_filename)
    print(f"QR code generated and saved as '{qr_code_filename}'")