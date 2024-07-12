import qrcode

img = qrcode.make("https://youtu.be/LEtP7HgGTu0?si=cBl-4xx7Cw0_AZq0")
img.save("qr.png", "PNG")
