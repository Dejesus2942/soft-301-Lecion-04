opcion_general = "Si"

total_ventas_del_dia =  0
total_helados_vendidos = 0
total_batidos_vendidos = 0

while opcion_general == "Si":
    print("Entradas:")
    print()
    print("Pedido del cliente")
    ap = input("Apellido del cliente: ")
    tpvp = input("Tiene tarjeta PuraVidaPops (Si/No): ")
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
    else:
        print("Error en valor, verificar")
    print(str(pph) + " colones por helados")
    if cfb == 1:
        ppb = 1200 * cbd
    elif cfb == 2:
        ppb = 1300 * cbd
    elif cfb == 3:
        ppb = 1400 * cbd
    else:
        print("Error en valor, verificar")
    print(str(pph) + " colones por batidos")
    tsd = pph + ppb
    print("Total sin descuento " + str(tsd))
    dap = tsd * .10 if ap == "Alvarado" else 0
    print("Descuento por apellido del día: " + str(int(dap)))
    dpvp = tsd * .15 if tpvp == "Si" else 0
    print("Descuento por PuraVidaPops : " + str(int(dpvp)))
    tp = (tsd - dap) - dpvp
    print("Total a pagar " + str(int(tp)) + " colones")

    total_ventas_del_dia += tp
    total_helados_vendidos += cdh
    total_batidos_vendidos += cbd

    opcion_general = input("Desea atender oto cliente (Si/No): ")

print("Reporte final del día para Heladería POPS®")
print("-----------------------------------------------------")
print("Total de ventas de día: " + str(int(total_ventas_del_dia)) + " colones")
print("Total de helados vendidos: " + str(total_helados_vendidos))
print("Total de batidos vendidos: " + str(total_batidos_vendidos))