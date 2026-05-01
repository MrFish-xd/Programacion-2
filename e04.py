# Una bacteria se reproduce en un lapso de una hora
# Luego, por cada hora que pasa cada acteria se reproduce en otra
# preguntar al usuario cuantas horas pasaron e indicar cuantas bacterias habrá

horas = int(input("¿Cuántas horas pasaron? "))
bacterias = 2 ** horas

print(f"Después de {horas} hora(s), habrá {bacterias} bacteria(s).")
