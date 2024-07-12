import qrcode

img = qrcode.make("https://youtu.be/_3HFNqforiM?si=KchFGSUo-q02qIe5")
img.save("qr2.png", "PNG")
