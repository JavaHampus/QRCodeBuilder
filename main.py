import os
import qrcode
from PIL import Image
from winotify import Notification, audio

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

redirect_url = input("Where would you like the QR Code to redirect too?").lower()
qr.add_data(redirect_url)
qr.make(fit=True)

img = qr.make_image(fillcolor="Black")

img.save(f'QR-Code.png')

notification = Notification(
    app_id="Created by AnkanMod",
    title="QRCode Builder",
    msg="Your QR Code has been generated."
)

notification.show()





