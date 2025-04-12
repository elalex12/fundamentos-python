def calculadora(a, b, operacion):
    operaciones ={
        'suma': a + b,
        'resta': a - b,
        'multiplicacion': a * b,
        'division': a / b if b !=0 else"Error: Division por 0 imposible" 

    }
    return operaciones.get(operacion, "operacion no valida")
print(calculadora(10,5,'suma'))
print(calculadora(10,5,'resta'))
print(calculadora(10,5,'multiplicacion'))
print(calculadora(10,5,'division'))