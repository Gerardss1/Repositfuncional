import qrcode
texto= input("dimeel texto del QR:")
img = qrcode.make(texto)

textoimg = input("dime el nombre de la imagen para el QR:")
img.save(textoimg + ".png")