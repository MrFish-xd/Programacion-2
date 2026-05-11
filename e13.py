# Implementar en python una funcion para aplicar cifrado cesar a una cadena.
# Se debe pasar el mensaje y el desplazamiento como parametros.
# La misma funcion debe descifrar el mensaje si aplica un desplazamiento negativo.

mensaje = input("Ingrese el mensaje a descifrar: ")
codigo = int(input("Ingrese el desplazamiento: "))
despla = list(mensaje)

def(cesar):
    cifrado = ""
    for i in range(len(despla)):
        cifrado = ord(despla[i])
        cifrado += codigo
        
        
        
        
    