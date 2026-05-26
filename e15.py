#Importar en Python una imagen en escala de grises y almacenarla en una matriz.
# Mostrar la imagen en pantalla. Luego ordenar los valores numéricos para voltear la imagen horizontalmente y mostrar el resultado en pantalla

# Para ejecutarlo, hace falta tener la imagen, y descargar las librerías necesarias, como numpy, matplotlib y PIL

import numpy as np # Importa la libreria numpy y le asigna el alias "np"
import matplotlib.pyplot as plt # Importa la libreria matplotlib.pyplot y le asigna el alias "plt"
from PIL import Image, ImageOps # Importa la clase Image y el módulo ImageOps de la biblioteca PIL (Python Imaging Library) para trabajar con imágenes en Python

img = Image.open('Kirby.jpg') # Abre la imagen Usando PIL y la almacena en la variable img
img_g = ImageOps.grayscale(img) # Convierte la imagen a escala de grises Usando "ImageOps.grayscale()" y la almacena en la variable "img_g"
matriz = np.array(img_g) # Convierte la imagen a una matriz de numpy
aux = 0 # Variable auxiliar para almacenar temporalmente los valores de la matriz 

fyc = matriz.shape # Obtiene las dimensiones de la matriz (numero de filas y columnas) y las almacena en la variable "fyc"
row = fyc[0]
col = fyc[1]
mit = col//2 # Calcula la mitad del número de columnas y la almacena en la variable "mit"

for i in range (row): # Itera sobre cada fila de la matriz usando un bucle for que va desde 0 hasta el número de filas (row)
    for j in range (mit): # Itera sobre cada columna de la matriz hasta la mitad usando un bucle for que va desde 0 hasta la mitad del número de columnas (mit)
        aux = matriz [i][j] # Almacena temporalmente el valor de la matriz en la posición actual (i, j) en la variable auxiliar "aux"
        ind_con = -(j + 1) # Calcula el índice de la columna opuesta a la posición actual (i, j) usando la fórmula "-(j + 1)" y lo almacena en la variable "ind_con"
        matriz[i][j] = matriz[i][ind_con] # Asigna el valor de la posición opuesta a la posición actual
        matriz[i][ind_con] = aux # Hace swap con el valor de la posición actual (i, j) con el valor en la posición opuesta (i, ind_con) usando "aux" para almacenar temporalmente uno de los valores durante el intercambio
plt.imshow(matriz, cmap='gray') # Convierte los numeros de "matriz" en la imagen en escala de grises
plt.title('-- Imagen volteada --') # Agrega un título a la imagen volteada horizontalmente
plt.axis('off') # Oculta los ejes de la imagen
plt.show() # Muestra la imagen volteada horizontalmente