import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)

qr.add_data("https://www.google.com/search?q=dictionary+english+to+hindi&rlz=1C1JJTC_enIN998IN998&oq=dictio&aqs=chrome.1.0i131i433i512j0i512j69i57j0i433i512l5j0i433i650j0i512.5841j0j7&sourceid=chrome&ie=UTF-8")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color = "blue")
img.save("Google_Dictionary.png")