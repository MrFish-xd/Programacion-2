# Implementar en python una funcion para aplicar cifrado cesar a una cadena.
# Se debe pasar el mensaje y el desplazamiento como parametros.
# La misma funcion debe descifrar el mensaje si aplica un desplazamiento negativo.

#---

# Esta funcion, toma un mensaje, y un codigo de desplazamiento para devolver el mensaje cifrado o descifrado, dependiendo del valor del codigo. Los unicos caracteres que no desplaza son el espacio y los caracteres especiales.
# Este codigo no cifra la Ñ, ni los caracteres acentuados, pero se puede modificar para incluirlos si es necesario.
def cifrado_cesar(mensaje, codigo):
    resultado = ""
    desplazamiento = list(mensaje)
    for i in range(len(desplazamiento)):
        if desplazamiento[i].isspace(): # Si el caracter es un espacio, se agrega al resultado sin modificarlo.
            resultado += desplazamiento[i]
        elif desplazamiento[i].isupper(): # Si el caracter es una letra mayuscula, se aplica el cifrado cesar utilizando el codigo de desplazamiento, y se agrega al resultado.
            resultado += chr((ord(desplazamiento[i]) + codigo - 65) % 26 + 65)
        elif desplazamiento[i].islower():# Si el caracter es una letra minuscula, se aplica el cifrado cesar utilizando el codigo de desplazamiento, y se agrega al resultado.
            resultado += chr((ord(desplazamiento[i]) + codigo - 97) % 26 + 97)
        else: # Si el caracter es un caracter especial, se agrega al resultado sin modificarlo.
            resultado += desplazamiento[i]
    return resultado

mensaje = input("Ingrese el mensaje a descifrar: ")
codigo = int(input("Ingrese el desplazamiento: "))
print(cifrado_cesar(mensaje, codigo))