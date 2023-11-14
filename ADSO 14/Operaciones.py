# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:01:25 2023

@author: FORMACION
"""

class Persona:
    
    def imprimirNombre():
         print("Sapo")
         
    def sumararNumero():
        print("Introduzca dos números para sumarlos")
        numero1 = input("Introduzca el primer número: ")
        numero2 = input("Introduzca el segundo número: ")
        suma = int(numero1) + int(numero2)
        print("La suma de los dos números es:", suma)
 
class Geometria:
    def areaTriangulo():    
       print("Introduzca la Base y la Altura del Triangulo")
       Base = input("Introduzca el numero de la base:")
       Altura = imput("Introduzca el numero de la altura:")
       opera = int(Base) * int(Altura)/2
       print ("El area del triangulo es:",opera)
       
       
       
       
Geometria. areaTriangulo()         
Persona.imprimirNombre()     
Persona.sumararNumero()