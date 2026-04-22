# conversor decimal - binario - hexadecimal
# diseñar un programa en el que el usuario ingrese un número
# y que eliga desde que sistema hacia que sistema de numeracion
# ademas mostara el caracter ASCII que corresponda al numero

#numero de opcion
num_op=1
#numero del usuario
num_user=0

print(' Presione -1- para convertir de decimal a bin\n Presione -2- para convertir de decimal a hexadecimal \n Presione -3- para convertir de binario a decimal\n Presione -4- para convertir de binario a hexadecimal\n Presione -5- para convertir de hexadecimal a decimal\n Presione -6- para convertir de hexadecimal a binario')

while (num_op >= 1):
    num_op = int(input('Ingrese la opcion: '))
    
    num_user=int(input('Ingrese el numero a convertir: '))
    
    if (num_op == 1):
        print(bin(num_user))
        
    elif (num_op == 2):
        print(hex(num_user))
    
    elif (num_op == 3):
        print('0d',num_user)
        
    elif (num_op == 4):
        print(hex(num_user))
        
    elif (num_op == 5):
        print(hex(num_user))
        
    elif (num_op == 6):
        print('0d',num_user)
        
    else:
        print('ingrese un numero dentro de las opciones ')
        
        break
    
    num_op=0
    
print('su numero en ASCII es: ', chr(num_user))