Dinero = float(input("Cant. de dinero ingresado: "))
Usuario = input("Nombre: ")

print(f"{Usuario} tiene {Dinero}$ en su cuenta de ahorros")
print(f"Cantidad de ahorros tras el primer año {Dinero*(1+4/100)**1:.2f}$")
print(f"Cantidad de ahorros tras el segundo año {Dinero*(1+4/100)**2:.2f}$")
print(f"Cantidad de ahorros tras el tercer año {Dinero*(1+4/100)**3:.2f}$")
