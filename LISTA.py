def cuerpo():
    print("Los datos de la lista son los siguientes:")
    print(datos)
    print("¿Quieres cambiar los datos? SI / NO")
    dec = input()
    if dec == "SI":
        print("¿Que quieres cambiar?")
        print("ID / APELLIDO / NOMBRE / EDAD / COLOR")
        dec2 = input()
        if dec2 == "ID":
            print("Ingresa el nuevo ID:")
            datos[0] = int(input())
        if dec2 == "APELLIDO":
            print("Ingresa el nuevo apellido:")
            datos[1] = input()
        if dec2 == "NOMBRE":
            print("Ingresa el nuevo nombre:")
            datos[2] = input()
        if dec2 == "EDAD":
            print("Ingresa la nueva edad:")
            datos[3] = int(input())
        if dec2 == "COLOR":
            print("Ingresa el nuevo color:")
            datos[4] = input()
        else:
            print("Opcion no valida")
    elif dec == "NO":
        CERRAR = False
    else:
        print("Opcion no valida")

if __name__ == '__main__':
    CERRAR = True
    datos = [000, "Apellido", "Nombre", 00, "Color"]
    while CERRAR == True:
        cuerpo()