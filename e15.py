#Importar en Python una imagen en escala de grises y almacenarla en una matriz.
# Mostrar la imagen en pantalla. Luego ordenar los valores numéricos para voltear la imagen horizontalmente y mostrar el resultado en pantalla

# Para ejecutarlo, hace falta tener la imagen, y descargar las librerías necesarias, como numpy, matplotlib y PIL

import numpy as np # Importa la biblioteca numpy y se le pone el alias np para facilitar su uso en el código
import matplotlib.pyplot as plt # Importa la biblioteca matplotlib.pyplot y se le pone el alias plt para facilitar su uso en el código
from PIL import Image, ImageOps # Importa la clase Image y el módulo ImageOps de la biblioteca PIL (Python Imaging Library) para trabajar con imágenes en Python

img = Image.open('Kirby.jpg') # Abre la imagen utilizando PIL y la almacena en la variable img
img_g = ImageOps.grayscale(img) # Convierte la imagen a escala de grises utilizando "ImageOps.grayscale()"" y la almacena en la variable "img_g"
matriz = np.array(img_g) # Convierte la imagen a una matriz de numpy

plt.imshow(matriz, cmap='gray') # Convierte los numeros de "matriz" en la imagen en escala de grises
plt.title('-- Imagen en escala de grises -- \n (Cierra para ver la imagen volteada)') # Agrega un título a la imagen en escala de grises
plt.show() # Muestra la imagen en pantalla en escala de grises

matriz_volteada = np.fliplr(matriz) # Da vuelta horizontal a la imagen utilizando "np.fliplr()"" y muestra la imagen volteada en escala de grises
plt.imshow(matriz_volteada, cmap='gray') 
plt.title('-- Imagen volteada --') # Agrega un título a la imagen volteada horizontalmente
plt.show() # Muestra la imagen volteada horizontalmente