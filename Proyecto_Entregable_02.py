print("Entradas:")
print()
print("Pedido del cliente")
ap = input("Apellido del cliente: ")
tpvp = input("Tiene tarjeta PuraVidaPops: ")
cdh = int(input("Cantidad de heldos: "))
sdh = input("Sabor de los helados: ")
cbd = int(input("Cantidad de batidos: "))
cfb = int(input("Cantidad de frutas de los batidos: "))
print()
print("Salidas:")
print("La cuenta del cliente es:")
print()
if sdh == "vainilla":
    pph = 600 * cdh
elif sdh == "chocolate":
    pph = 700 * cdh
elif sdh == "caramelo":
    pph = 750 * cdh
elif sdh == "fresa":
    pph = 800 * cdh
print(str(pph) + " colones por helados")
if cfb == 1:
    ppb = 1200 * cbd
elif cfb == 2:
    ppb = 1300 * cbd
elif cfb == 3:
    ppb = 1400 * cbd
print(str(pph) + " colones por batidos")
tsd = pph + ppb
print("Total sin descuento " + str(tsd))
dap = tsd * .10 if ap == "Alvarado" else 0
print("Descuento por apellido del día: " + str(int(dap)))
dpvp = tsd * .15 if tpvp == "sí" else 0
print("Descuento por PuraVidaPops : " + str(int(dpvp)))
tp = (tsd - dap) - dpvp
print("Total a pagar " + str(int(tp)) + " colones")