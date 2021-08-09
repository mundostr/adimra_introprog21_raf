import qrcode as qr

URL = "https://itecrafaela.edu.ar"

# codigoQr = qr.QRCode(error_correction=qr.constants.ERROR_CORRECT_H)
# codigoQr.add_data(URL)
# codigoQr.make(fit=True)

# imagenQr = codigoQr.make_image(fill_color="black", back_color="white")
# imagenQr.save("semana15/codigo_qr.png")

# print("Código generado")

imagen = qr.make(URL)
imagen.save("semana15/codigo_qr.png")
