
def t_d_r(operacion):
    num = int(input("introduzca un numero:"))
    
    operaciones={
        'doble' : num * 2,
       'triple' : num * 3,
       'raiz' : num ** 0.5,   
      }                         
     
    
    return operaciones.get(operacion,"operacion novalida")                                                             
print(" el resultado del doble es :",(t_d_r('doble')))
print("el resultado del triple es: ",(t_d_r('triple')))
print(" el resultado de la raiz es : ",(t_d_r('raiz')))
