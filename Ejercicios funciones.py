# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:02:57 2020

@author: Desarrollos Vip

def producto(n1,n2):
    return n1 * n2


print(producto(3,8))


#2

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

print(producto(n1,n2))


#3

def rectangulo(base,altura):
    return 2 * (base * altura)

print(rectangulo(4,9))



for i in range(5):
    print (i * i)
    
for i in range(2,5):
    print(i,2 ** i)


#5

def factorial(n):
    factorial = 1;
    if n == 0:
        return 1
    
    for i in range(1,n+1):
        factorial = factorial * i
       
        
    return factorial

print(factorial(10))


#6
#a

def calc(n1,n2):
    
    print("Suma = ",int(n1 + n2))
    print("Resta= ",int(n1 - n2))
    print("Producto = ",int(n1 * n2))
    if n2 != 0:
        print("Division = ",int(n1 / n2))
        
calc(10,5)

#b

def tabla(n):
    print("---------------------------------")
    print("        La tabla del ",n)
    print("---------------------------------")
    for i in range(10+1):
        print(n," x ",i," = ",n*i)
        

tabla(9)

"""

def mil(palabra):
    
    for i in range(1001):
        print(palabra,end=" ")
    

mil("hola mundo")













    