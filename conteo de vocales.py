cadena = "Hola mundo"
vocales = "aeiouAEIOU"
contador=sum(1 for letra in cadena if letra in vocales)
print("numero de vocales:",contador)