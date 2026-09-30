MAX_INTENTOS = 3
def main() -> None:

    pin_correcto = None
    while pin_correcto is None:
        try:
            pin_correcto = int(input("PIN correcto: "))
        except ValueError:
            print("Escribe un número entero...")

    intentos = 0
    acceso_concedido = False

    while intentos < MAX_INTENTOS and not acceso_concedido:
        try:
            pin_tecleado = int(input(f"PIN (intento {intentos + 1}): "))
            intentos += 1

            if pin_tecleado == pin_correcto:
                acceso_concedido = True

        except ValueError:
            print("Escribe un número entero...")

    if acceso_concedido:
        mensaje = "ACCESO"
    else:
        mensaje = "DENEGADO"

    print(mensaje)

if __name__ == "__main__":
    main()