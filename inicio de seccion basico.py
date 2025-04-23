usuario = "admin"
clave = "1144"

User = input("Introdusca un usuario:  ")
password = input("Introduce una contraseña: ")

if User == usuario and password == clave:
    print("ingreso de seccion exitoso")
else:
    print("acceso denegado")