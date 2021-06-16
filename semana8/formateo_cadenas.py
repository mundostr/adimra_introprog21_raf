# Valores de prueba para ver distintas opciones de formateo de cadenas
# Estas opciones serán muy útiles para formatear al momento de escribir a una base de datos,
# enviar un texto JSON o en otros formatos standard para intercambio.
promedio1 = 382.4
promedio2 = 340.05

# Para desarrollo y depuración, podemos aplicar simplemente la opción "plana", imprimiendo
# el / los nombres de variables que necesitamos. Si debemos imprimir varios en una misma línea,
# solo los separamos por comas -> print(promedioSemestre1, promedioSemestre2, etc)
print(promedio1, promedio2)

# Esta es otra variante, del lado izquierdo colocamos un "título", y luego las variables a mostrar,
# con la misma idea del caso anterior. Si es más de una, separaremos por comas.
print("Promedios:", promedio1, promedio2)

# En este caso estamos formando un texto único, "concatenando eslabones" mediante el signo +.
# Lógicamente las partes que ya sean cadenas se escriben de forma directa, y las que no, se
# convierten utilizando la función str(), caso contrario el intérprete generará un error al
# momento de evaluar el comando.
# Esta es una opción bastante tradicional, pero no resulta muy limpia ni intuitiva, además
# de generar una carga extra para el sistema al momento del manejo de datos.
print("Promedios: $ " + str(promedio1) + " AR y $ " + str(promedio2) + " AR")

# Esta alternativa es más actual y "limpia", porque no necesitamos realizar el casting, es decir
# las conversiones a cadena. Tan solo armamos un único texto del lado izquierdo, con "placeholders".
# En este caso los placeholders se especifican con llaves y un índice, comenzando en 0. Si en la
# cadena se desea colocar 3 variables, los placeholders serán {0}, {1} y {2}, y en forma()
# listaremos las variables separadas por comas.
print("Promedios: $ {0} AR y $ {1} AR".format(promedio1, promedio2))

# Format permite además agregar otros indicadores para completar el placeholder
# En este ejemplo, garantizamos que siempre la cifra se muestre con 2 decimales.
# Los índices (0, 1, etc) en los "placeholder", pueden omitirse, el sistema insertará
# los valores respetando el orden en el que se indican las variables en format().
print("Promedios: $ {0:.2f} AR y $ {1:.2f} AR".format(promedio1, promedio2))

# Lo repasado de format(), es válido también para el uso de la macro f, con la cual
# podemos generar una cadena aún más limpia y compacta. El último print, podría reescribirse
# de la siguiente forma:
print(f"Promedios: $ {promedio1:.2f} AR y $ {promedio2:.2f} AR")
