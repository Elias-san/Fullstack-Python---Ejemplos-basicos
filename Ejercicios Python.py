# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:01:23 2020

@author: Desarrollos Vip

# 1)

print("Hola Mundo")

# 2)

print(3+5)

# 3)

nombre = input("Ingrese nombre: ")
print("Hola ",nombre)

#4)
num1 = int(input("Ingrese un numero: "))
num2 = int5(input("Ingrese otro numero: "))
print("La suma de ambos es: ", num1 + num2)


# 5)
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2:
    print(num1," Es el numero mayor")
else:
    if num2 > num1:
        print(num2," Es el numero mayor")
    else:
        print("Los numeros son iguales")



# 6)
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese el ultimo numero: "))

if num1 > num2:
    print(num1," Es el numero mayor")
elif num2 > num1:
    print(num2," Es el numero mayor")
elif num3 > num2:
    print(num3," Es el numero mayor")
    

# 7)
num = int(input("Ingrese un numero: "))

if num % 2 == 0 :
    print(num," Es divisible por 2")
else:
    print("Es impar")
    

# 8)
letra = 0
frase = input("Ingrese frase: ")
indice = 0
for x in frase:
    if frase[indice] == "a":
        letra = letra + 1
    
    indice = indice + 1

print("La frase tiene ", letra , " a")



# 9)

frase = input("Ingrese frase: ")
a = False
e = False
i = False
o = False
u = False

for x in frase:
    if (x =="a") and (a != True):
        a = True
        print(x)
    elif (x=="e") and (e != True):
        e = True
        print(x)
    elif (x=="i") and (i != True):
        i = True
        print(x)
    elif (x=="o") and (o != True):
        o = True
        print(x)
    elif (x=="u") and (u != True):
        u = True
        print(x)




# 10)
vocal = 0
frase = input("Ingrese frase: ")
indice = 0
for x in frase:
    if (frase[indice] == "a") or (frase[indice] == "e") or (frase[indice] == "i") or (frase[indice] == "o") or (frase[indice] == "u"):
        vocal = vocal + 1
    
    indice = indice + 1

print("La frase tiene ", vocal , " vocales")




#11

frase = input("Ingrese frase: ")
a = 0
e = 0
i = 0
o = 0
u = 0

for x in frase:
    if (x =="a"):
        a = a + 1
    elif (x=="e"):
        e = e + 1
    elif (x=="i"):
        i = i + 1
    elif (x=="o"):
        o = o + 1
    elif (x=="u"):
        u = u + 1

print("La frase ",frase, " tiene ", a," a ",e," e ",i," i ",o," o , y ", u," u")

"""
# 12

numero = int(input("Ingrese numero"))
divisible = "divisible por "

if (numero % 2 == 0):
    divisible = divisible + " 2."
if (numero % 3 == 0):
    divisible = divisible + " 3."
if (numero % 5 == 0):
    divisible = divisible + " 5."
if (numero % 7 == 0):
    divisible = divisible + " y 7."


print("El numero ",numero," es ",divisible)











