num1 = int(input("introduce un numero para la suma: "))
num2 = int(input("introduce otro:  "))

respuesta = input("desea hacer la suma : ")

if respuesta == "si" or respuesta == "Si":
    print("el resultado de la suma es: ",num1 + num2)   
else:
   print("no se realizara la suma")