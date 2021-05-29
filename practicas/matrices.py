# # LISTA, "mutable"
# variableUnitaria = 23
# listaVariables = [23, 15, 1000, 0, -2]
# print(listaVariables)
# print(listaVariables[1])
# listaVariables.append(300)
# print(listaVariables)
# listaVariables.remove(15)
# print(listaVariables)
# listaVariables[1] = 2000
# print(listaVariables)


# # TUPLA, "inmutable"
# tuplaVariables = (23, 15, 1000, 0, -2)
# tuplaDias = ("Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom")
# print(tuplaVariables)
# print(tuplaVariables[2])
# tuplaVariables.add(15) # NO va a funcionar al ser inmutable


# Diccionarios, "parcialmente inmutable"
datosPersonales = { "codigo": 1344, "apellido": "Perren", "nombre": "Carlos", "saldo": 34620 }
print(datosPersonales)
print(datosPersonales["codigo"])
datosPersonales["codigo"] = 1345
print(datosPersonales)
datosPersonales.pop("codigo", None)
print(datosPersonales)
datosPersonales["tipoCuenta"] = 3
print(datosPersonales)
