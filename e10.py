# Escribir una funcion para convertir temperatura de celsius a fahrenheit
# y otra funcion para la conversion opuesta

# Formula (celsius*1,8)+32

def temp_f (c):
    valor_fahrenheit = (c * 1.8) + 32
    return valor_fahrenheit

def temp_c (f):
    valor_celsius = (f - 32) / 1.8
    return valor_celsius

celsius = int(input('Ingresa un valor en grados Celsius: '))
fahrenheit = int(input('Ingresa un valor de grados Fahrenheit: '))

print(f'El valor de: {celsius}ºC, es de: {temp_f(celsius)}ºF')
print(f'El valor de: {fahrenheit}ºF, es de: {temp_c(fahrenheit)}ºC')
