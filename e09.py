# Escribir una funcion donde el usuario ingresa un numero entero prositivo (validarlo)
# Y calclar el factorial

def num_positivo ():
    while True:
        try:
            num = int(input('Ingresa un numero positivo para calcular el factorial: '))
            if num >= 0:
                return num
            else:
                print('El numero tiene que ser positivo. Intentalo de nuevo.')
        except ValueError:
            print('Ingresa un numero entero. Intenta de nuevo.')
            
def factorial (num):
    resultado = 1
    for i in range (1, num + 1):
        resultado *= i
    return resultado

numero = num_positivo()

print(f'El factorial de: {numero} es: {factorial(numero)}')