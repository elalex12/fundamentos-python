num = int(input("introduce un numero:"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es primo")
            break
    else:
         print(num, "es primo")
else:
    print(num,"no es primo")
