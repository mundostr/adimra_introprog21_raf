# Repasamos los 3 tipos más habituales en Python para el manejo de colecciones de datos

# LISTA, "mutable"
# Una lista es modificable, puede contener todos los items del mismo tipo o de diferentes tipos
# Se genera utilizando corchetes y se accede mediante índice que comienza desde 0.
variableUnitaria = 23
listaVariables = [23, 15, 1000, 0, -2]
print(listaVariables)
print(listaVariables[1])
listaVariables.append(300)
print(listaVariables)
listaVariables.remove(15)
print(listaVariables)
listaVariables[1] = 2000
print(listaVariables)


# TUPLA, "inmutable"
# Una tupla por su parte no es modificable, si intento utilizar algún método para alterar sus contenidos,
# como por ejemplo el add(15) de la línea 25, el intérprete generará un error
# Se genera utilizando paréntesis y al igual que las listas, se accede mediante índice que comienza desde 0.
tuplaVariables = (23, 15, 1000, 0, -2)
tuplaDias = ("Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom")
print(tuplaVariables)
print(tuplaVariables[2])
tuplaVariables.add(15) # NO va a funcionar al ser inmutable


# Diccionarios, "parcialmente inmutable"
# Un diccionario se arma con pares identificador: valor, separados por comas.
# Es una forma alternativa para guardar datos de diversos tipos sobre un mismo objeto.
# Se genera utilizando llaves, y se accede a cada valor indicando el identificador, lo cual resulta más
# intuitivo en muchos casos que utilizar el índice.
datosPersonales = { "codigo": 1344, "apellido": "Perren", "nombre": "Carlos", "saldo": 34620 }
print(datosPersonales)
print(datosPersonales["codigo"])
datosPersonales["codigo"] = 1345
print(datosPersonales)
datosPersonales.pop("codigo", None)
print(datosPersonales)
datosPersonales["tipoCuenta"] = 3
print(datosPersonales)
