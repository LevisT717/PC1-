
Edad = int(input("¿Cuántos años tienes?: "))

if Edad < 4:
    print("Precio: Entrada gratis")
elif 18 > Edad > 4:
    print("Precio: 5$")
elif Edad > 18:
    print("Precio: 10$")