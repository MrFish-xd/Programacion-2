# Conversor decimal - binario - hexadecimal

print("""
 Presione -1- para convertir de decimal a binario
 Presione -2- para convertir de decimal a hexadecimal
 Presione -3- para convertir de binario a decimal
 Presione -4- para convertir de binario a hexadecimal
 Presione -5- para convertir de hexadecimal a decimal
 Presione -6- para convertir de hexadecimal a binario
""")

num_op = int(input('Ingrese la opcion: '))

if num_op in (1, 2):
    num_user = int(input('Ingrese el número en decimal: '))

elif num_op in (3, 4):
    num_user = int(input('Ingrese el número en binario: '), 2)

elif num_op in (5, 6):
    num_user = int(input('Ingrese el número en hexadecimal: '), 16)

else:
    print('Opción inválida.')
    num_user = None

if num_user is not None:
    if num_op == 1:
        print('Binario:', bin(num_user))
    elif num_op == 2:
        print('Hexadecimal:', hex(num_user))
    elif num_op == 3:
        print('Decimal:', num_user)
    elif num_op == 4:
        print('Hexadecimal:', hex(num_user))
    elif num_op == 5:
        print('Decimal:', num_user)
    elif num_op == 6:
        print('Binario:', bin(num_user))

    if 0 <= num_user <= 1114111:
        print('Su número en ASCII es:', chr(num_user))
    else:
        print('El número está fuera del rango ASCII válido.')