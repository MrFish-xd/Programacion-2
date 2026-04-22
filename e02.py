import random
secret=random.randint(1,20)
vidas=6

while(vidas != -1):
    
    num_user=int(input('Ingrese un numero al azar, para adivinar el secreto\n  '))    
    
    if (num_user > secret):
        print(f'El numero secreto es Menor que el ingresado\n Tienes {vidas} restantes\n')
        vidas-=1
        
    elif (num_user < secret):
        print(f'El numero secreto es Mayor que el ingresado\n Tienes {vidas} restantes\n')
        vidas-=1
    elif (vidas==0):
        print('Perdiste, vuelve a internatlo')
        break
    else:
        print("ADIVINASTE EL NUMERO")
        break
    