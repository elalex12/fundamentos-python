
def calculadora2(operacion):
    a = int(input("introduce un numero "))
    b = int(input("introduce otro:  "))
    operaciones ={
        'suma': a + b,
        'resta': a - b,
        'multiplicacion': a * b,
        'division': a / b if b !=0 else"Error: Division por 0 imposible" 

    }
    return operaciones.get(operacion, "operacion no valida")
print("el resultado de la suma es : ",(calculadora2('suma')))
print(" el resultado de la resta es :",(calculadora2('resta')))
print("el resultado de la multiplicacion es: ",(calculadora2('multiplicacion')))
print(" el resultado de la division es : ",(calculadora2('division')))

