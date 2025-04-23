numeros = []
suma = 0
while True:
    n = int(input("escribe un numero(0 para terminar)"))
    if n == 0:
     break
    numeros.append(n)
    suma += n
print("la suma total es :", suma)