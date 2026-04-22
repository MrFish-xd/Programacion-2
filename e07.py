# Diseñar un programa que pida la fecha de nacimoento del usuario e indique su edad en 2 formatos
# cantidad de dias totales, y años-meses-dias. Mostrar pantalla la fecha de nacicieno en formato epoch/timestamp

import datetime

year = int(input('Ingresa tu año de nacimiento: '))
month = int(input('\nIngresa tu mes de nacimiento: '))
day = int(input('\nIngresa tu dia de nacimiento: '))

now = datetime.date.today()
born = datetime.date(year, month, day)

day_total = now - born
day_total = day_total.days
util = day_total // 365
util_m = day_total % 365

year_now = util
month_now = util_m // 30
day_now = util_m % 30


print(f'\nTienes {day_total} dias de nacido, {year_now} años, {month_now} meses, {day_now} dias')