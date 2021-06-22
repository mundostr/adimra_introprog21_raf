import re
import requests as req
import consulta_api as remoto

consultaRemota = req.get(remoto.RUTA_API)
resultado = remoto.filtrarInfoRemota(consultaRemota, "texto", "\n", remoto.EXPRESION_REGULAR)
print(resultado)
