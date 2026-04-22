# Escribir una funcion que calcule el area de un circulo,
# Luego escribir una funcion que calcule el volumen de un cilindro llamando a la primera funcion

import math

def area_circulo (r):
    area = math.pi * r ** 2
    return area

def volumen_cilindro (r, h) :
    volumen = area_circulo(r) * h
    return volumen

radio = float(input('Ingrese el Radio del circulo: '))
altura = float(input('Ingresa la altura del cilindro: '))

print(f'El area del circulo con radio {radio} es: {area_circulo(radio):.2f}')
print(f'El volumen del cilindro es: {volumen_cilindro(radio, altura):.2f}')

