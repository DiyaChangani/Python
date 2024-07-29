import qrcode
import image

qr = qrcode.QRCode(
    version = 10,
    box_size = 6,
    border = 5
)

data = "Hello, this is my qrcode project in python."

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
