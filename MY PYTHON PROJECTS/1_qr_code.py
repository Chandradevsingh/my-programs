import qrcode as qr


img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")

img.save("wscube_tech_youtube_channel_qr_code.png")