import math

# Pedir coeficientes al usuario
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Verificar que a no sea 0 (si lo es, no es cuadrática)
if a == 0:
    print("No es una ecuación cuadrática (a no puede ser 0).")
else:
    # Calcular discriminante
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"La ecuación tiene dos soluciones reales: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif D == 0:
        x = -b / (2*a)
        print(f"La ecuación tiene una solución real doble: x = {x:.2f}")
    else:
        print("Ecuación no presenta solución real")