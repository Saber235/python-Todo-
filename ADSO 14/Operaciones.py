# -*- coding: utf-8 -*-
"""
Programacion orientada a obgetos"___________"
Herencia "____"
Polimorfismo "_____"
Encapsulamiento "______"

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

# Clase padre
class Espada:
    def __init__(self, daño: int, durabilidad: int, velocidad_ataque: float):
        self.daño = 4
        self.durabilidad = 100
        self.velocidad_ataque = 1.2

    def golpear(self, objetivo):
        objetivo.vida -= self.daño
# Clases hijas
class EspadaLlama(Espada):
    def __init__(self):
        super().__init__()
        self.daño = 7
        self.durabilidad = 200
        self.velocidad_ataque = 1.7
        self.puede_causar_dano_por_fuego = True       

    def golpear(self, objetivo):
        objetivo.vida -= self.daño


Geometria.areaTriangulo()
Persona.imprimirNombre()
Persona.sumarNumeros()
