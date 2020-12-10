# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:23:11 2020

@author: Desarrollos Vip



class Alumno:
     
     def __init__(self,nombre,apellido,legajo,edad,materias):
         self.nombre=nombre
         self.apellido=apellido
         self.legajo=legajo
         self.edad=edad
         self.materias=materias
     
     
m=Alumno("Estela","Gonzalez",27654,20,3)

print(m)
"""

class Persona:
    
    def __init__(self,nombre,apellido,legajo,edad,materias):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mayor(nombre,apellido,edad):
        if edad > 18 :
            print("El alumno ",Persona.nombre," ",Persona.apellido," ", "es mayor de edad")
    
curso = []
for i in range(0,2):
        
    Persona.nombre = input("Ingrese nombre de alumno:  ")
    Persona.apellido = input ("Ingrese apellido del alumno: ")
    Persona.edad = int(input("Ingrese edad: "))
    Persona.mayor(Persona.nombre,Persona.apellido,Persona.edad)
    Persona.legajo = int(input("Ingrese legajo: "))
    Persona.materias = int(input("Ingrese cantidad de materias: "))
    curso.append(Persona)
    

for i in range(0,2):
    print(curso[i])

for i in range(0,2):
    print(curso[i])
    
    
    