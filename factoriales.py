num = int(input("escriba un numero:"))  # line 1

def factorial(num):                      # line 2
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(num))
