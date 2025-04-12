palabra = (input("Ingrese una palabra:"))
print("Es un palindromo" if palabra == palabra[::-1] else "No es un palindromo")