lista_etapas_lavado = ["Llenado", "Lavado", "Enjuague", "Drenado", "Listo"]
for elemento in lista_etapas_lavado:
    print(elemento)

    if elemento == "Llenado" or elemento == "Listo":
        print("Puedo abrir la puerta")
    else:
        print("No puede abrir la puerta")