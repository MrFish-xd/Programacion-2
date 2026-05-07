# Los estudiantes deben pasar al frente a exponer, pero nadie quiere pasar primero.
# Diseñar un programa con una lista con los nombres de los estudiantes, y de forma aleatoria
# generar otra lista que indique el orden en el que deben pasar a exponer.

# Ayuda: Usar bucle for i range(len(estudiantes)):
# Ayuda: Para añadir un elemento a una lista se puede usar el método append().
# Solo se puede usar random.randint() para generar un número aleatorio entre 0 y el tamaño de la lista de estudiantes, y se puede usar el for.

import random
estudiantes = ["Federico", "Hana", "Leonardo", "Ismael", "Danilo", "Valentin", "Mateo", "León", "Santiago", "Lucia"]
orden_exposicion = []
for i in range(len(estudiantes)):
    aleatorio = random.randint(0, len(estudiantes) - 1)
    orden_exposicion.append(estudiantes.pop(aleatorio))
    
print("El orden de exposición es:")
for i in range(len(orden_exposicion)):
    print(f"{i + 1}. {orden_exposicion[i]}")