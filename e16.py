# Importar una imagen a color y mostrarla.
# Definir una funcion para convertir imagenes a escala de grises y mostrar el resultado.
# No usar funciones integradas, en su lugar usar la formula: Gris = R*0.2989 + G*0.5870 + B*0.1140import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_color = Image.open("Kirby.jpg")
plt.imshow(img_color)
plt.title("--Imagen a Color--")
plt.axis('off')
plt.show()

def escala_grises(rt_img):
    img = Image.open(rt_img)
    ancho, alto = img.size
    
    img_gris = Image.new("L", (ancho, alto))
    pixeles_gris = img_gris.load()
    pixeles_color = img.load()
    
    for i in range(ancho):
        for j in range(alto):
            r, g, b = pixeles_color[i, j]
            gris = int(r * 0.2989 + g * 0.5870 + b * 0.1140)
            pixeles_gris[i, j] = gris
            
    return img_gris

img_resultado = escala_grises("Kirby.jpg")

plt.imshow(img_resultado, cmap='gray')
plt.title("--Imagen en Escala de Grises--")
plt.axis('off')
plt.show()