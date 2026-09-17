saldo = float(input("ingresa tu saldo actual:"))
retirado = float(input("ingresa cuanto has retirado hoy:"))
monto = float(input("ingresa el monto a retirar:"))

if monto % 50 != 0:
    print("MONTO NO VALIDO | SALDO:" , saldo)
elif monto > saldo:
    print("SALDO INSUFICIENTE | SALDO:" , saldo)
elif (retirado + monto) > 6000:
    print("LIMITE DIARIO EXCEDIDO | SALDO:" , saldo)
else:
    saldo = saldo - monto
    print("ENTREGADO | SALDO:" , saldo)
