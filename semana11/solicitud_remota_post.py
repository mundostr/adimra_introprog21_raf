import requests as req

URL = "http://pad19.com:3030/adimra21"

datos = { "apellido": "Pompin", "nombre": "Pepe" }

solicitud = req.post(URL, data=datos)

print(solicitud.json())
