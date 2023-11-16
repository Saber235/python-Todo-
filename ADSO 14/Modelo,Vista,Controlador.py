# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:17:11 2023

@author: FORMACION
"""

# triangulo rectangulo y circulo y salir clase llamada Areas
#y todos los metodos tienen que terminar con las iniciales de un que serian JG
# acomoda el clase area que acomode el codigo acorde a diagrama mvc
 
class Area:

      def __init__(self):
        pass
        
      def area_rectangulo(self,base,altura):
          return(base * altura)
    
      def area_triangulo(self, base, altura):
        return (base * altura) / 2
    
      def area_circulo(self, radio):
        return (3.14159 * radio ** 2)
    
      def salir(self):
        print("Gracias por usar la clase Area")


    def main():
      area = Area()
      #Calcular el area del  Rectangulo
      base = float(input("Ingrese la base del Rectangulo"))
      altura = float(input("Ingrese la altura del Rectangulo"))
      area_rectangulo = area.area_rectangulo(base, altura)
      print("El area del Rectangulo es:",area_rectangulo)
      
      # Calculamos el área del triángulo rectángulo
      base = float(input("Ingrese la base del triángulo: "))
      altura = float(input("Ingrese la altura del triángulo: "))
      area_triangulo = area.area_triangulo(base,altura)
      print("El área del triángulo es:",area_triangulo)
    
      # Calculamos el área del círculo
      radio = float(input("Ingrese el radio del círculo: "))
      area_circulo = area.area_circulo(radio)
      print("El área del círculo es:", area_circulo)
    
      # Salimos de la aplicación
      area.salir()


if __name__ == "__main__":
  main()