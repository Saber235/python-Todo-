# -*- coding: utf-8 -*-
"""
Programacion orientada a obgetos"___________"


"""
class Persona:
    
    def imprimirNombre():
         print("Sapo")
         
    def sumarNumeros():
        print("Introduzca dos números para sumarlos")
        numero1 = input("Introduzca el primer número: ")
        numero2 = input("Introduzca el segundo número: ")
        suma = int(numero1) + int(numero2)
        print("La suma de los dos números es:", suma)
 
class Geometria:
    def areaTriangulo():    
       print("Introduzca la Base y la Altura del Triangulo")
       Base = input("Introduzca el numero de la base:")
       Altura = input("Introduzca el numero de la altura:")
       opera = int(Base) * int(Altura) / 2
       print("El area del triangulo es:",opera)

Geometria.areaTriangulo()         
Persona.imprimirNombre()     
Persona.sumarNumeros()
