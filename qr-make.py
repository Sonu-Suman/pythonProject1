import qrcode
from qrcode import constants

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=10)

qr.add_data('https://www.iskcon.org/')
qr.make(fit=True)
img = qr.make_image(background='white', color='black')
img.save('like.png')