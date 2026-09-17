print("CAPTURA DE DATOS DEL PACIENTE")

temp = float(input("ingrese la temperatura:"))
fc = float(input("ingrese la frecuencia:"))
sat = float(input("ingrese la saturacion:"))

if sat < 90 or fc > 120:
    print("ROJO")
else:
    if temp >= 39:
        print("AMARILLO")
    else:
        print("VERDE")