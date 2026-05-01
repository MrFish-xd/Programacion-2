 # Un profe tiene 'X' caramelos y los quiere repartir entre 'Y' estudiantes.
# Los esudiantes reciben un numero entero de caramelos.
# Preguntar cuantos caramelos se reparten a tal cantidada de alumnos.
# Indicar cuantos caramelos le tocan a cada estudiante y cuantos sobran en la bolsa.

caramelos = int(input('Ingresá la cantidad de caramelos que tiene el profesor: '))
alumnos = int(input('Ingresá cuantos estudiantes hay en el aula: '))

if (alumnos >= 1 and caramelos >= 1):
    
    print('A cada alumno, se le reparte ', caramelos // alumnos)
    print('En la bolsa quedan ',caramelos % alumnos,' caramelos restantes')
else:
    print('La cantidad de alumnos y caramelos tiene que ser mayor a cero.')