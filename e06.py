# Un cajero automatico entrega solo billetes de $1000 y de $200
# ingresar la cantidad que desea extraer el usuario, y luego indicar cuantos billetes se le entregan al cliente
# Indicar el ademas el saldo que no se pudo extraer porque no hay billetes.
    
extraccion = int(input('Ingrese la cantidad de dinero que desea retirar: '))

billetes_1000 = extraccion // 1000      
resto_1      = extraccion % 1000        

billetes_200 = resto_1 // 200           
saldo_no_entregado = resto_1 % 200     

print(f'\nBilletes de $1000: {billetes_1000}')
print(f'Billetes de $200:  {billetes_200}')
print(f'Saldo no retirado: ${saldo_no_entregado}')