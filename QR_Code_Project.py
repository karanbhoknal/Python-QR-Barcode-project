# How to generate QR Code generator in Python
#import qrcode as qr

# we want in image formate that's why we have to declare variable name is img
#img=qr.make("copy the video url here")
#img.save("wscube_youtube.png") # write here qrcode name and png size it is simple way for qrcode


import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=4,)
                 


qr.add_data("https://drive.google.com/file/d/17DrYUVcNqlSqGU231TmyWHKGUXWGKa1W/view?usp=sharing") # paste here link
qr.make(fit=True) # 
img=qr.make_image(fill_color="red",back_color="blue")
img.save("ResumeBarcode.png")

