# declarar una matriz de 4 filas y 4 columnas con numeros enteros sucesivos a partir del 1 en cada celda.
# Calcular la suma y la multiplicacion de la diagonal principal y de la contra diagonal.
# Mostrar en pantalla estos  valores y los elementos de la matriz.

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

suma = 0
multi = 1

csuma = 0
cmulti = 1

for i in range(len(m)):
    for j in range(len(m)):
        if i == j:
            suma += m[i][j]
            multi *= m[i][j]
        elif i + j == len(m) - 1:
            csuma += m[i][j]
            cmulti *= m[i][j]

print(f"Suma diagonal principal: {suma}")
print(f"Multiplicación diagonal principal: {multi}")
print(f"Suma contra diagonal: {csuma}")
print(f"Multiplicación contra diagonal: {cmulti}")