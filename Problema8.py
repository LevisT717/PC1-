time = input("Ingrese la hora en formato HH:MM -> ")

hours, minutes = time.split(":")

hora = int(hours) + int(minutes) / 60

# Verificar los rangos de comida
if 7 <= hora <= 8:
    print("Es hora de desayunar.")
elif 12 <= hora <= 13:
    print("Es hora de almorzar.")
elif 18 <= hora <= 19:
    print("Es hora de cenar.")
