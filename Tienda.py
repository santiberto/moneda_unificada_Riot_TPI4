def ejecutar_tienda():
    seleccion_de_tienda = ""
    usuario = input("Ingrese su usuario: ")

    Lista_comseticos_LOL = []
    Lista_comseticos_Valorant = []
    Lista_comseticos_2XKO = []

    lista_a_revisar_LOL = []
    lista_a_revisar_Valorant = []
    lista_a_revisar_2xko = []
    lista_a_revisar_Valorant.append(usuario)
    lista_a_revisar_2xko.append(usuario)
    lista_a_revisar_LOL.append(usuario)

    salario_total = 0

    while seleccion_de_tienda != "0":
        print("\n========================================")
        print(f"Usuario: {usuario} | Saldo actual: ${salario_total} monedas")
        print("========================================")
        print("(0) Salir de la tienda")
        print("(1) Cargar monedas")
        print("(2) Tienda LOL")
        print("(3) Tienda Valorant")
        print("(4) Tienda 2XKO")

        seleccion_de_tienda = input("Seleccione a qué sección de la tienda le gustaría ir: ")

        # --- SECCIÓN 1: CARGAR MONEDAS ---
        while seleccion_de_tienda == "1":
            print("\n--- CARGAR MONEDAS ---")
            print(
                "(1) 1000 monedas --- $10 \n(2) 1500 monedas --- $12 \n(3) 2000 monedas --- $16 \n(4) 2500 monedas --- $20 \n(5) Volver al menú principal")
            seleccion_compra = input("Seleccione que desea comprar:  ")

            if seleccion_compra in ["1", "2", "3", "4"]:
                ingreso_usuario = input("Ingrese su usuario para confirmar: ")
                if usuario == ingreso_usuario:
                    if seleccion_compra == "1":
                        salario_total += 1000
                    elif seleccion_compra == "2":
                        salario_total += 1500
                    elif seleccion_compra == "3":
                        salario_total += 2000
                    elif seleccion_compra == "4":
                        salario_total += 2500
                    print(f"¡Monedas cargadas con éxito! Nuevo saldo: {salario_total}")
                else:
                    print("Error: Este usuario no coincide.")
                # Volvemos al menú principal en lugar de cerrar el programa
                seleccion_de_tienda = ""
            elif seleccion_compra == "5":
                seleccion_de_tienda = ""

        # --- SECCIÓN 2: TIENDA LOL ---
        while seleccion_de_tienda == "2":
            print("\n--- TIENDA LOL ---")
            print(
                "(1) Blitzcrank skin --- 750 monedas\n(2) Skin Jinx --- 1075 monedas \n(3) Skin Vi --- 560 monedas\n(4) Volver al menú principal")
            seleccion_compra = input("Seleccione que desea comprar: ")

            if seleccion_compra == "1":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 750:
                    salario_total -= 750
                    Lista_comseticos_LOL.append("Blitzcrank skin ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "2":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 1075:
                    salario_total -= 1075
                    Lista_comseticos_LOL.append("Skin Jinx ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "3":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 560:
                    salario_total -= 560
                    Lista_comseticos_LOL.append("Skin Vi ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "4":
                seleccion_de_tienda = ""

        # --- SECCIÓN 3: TIENDA VALORANT ---
        while seleccion_de_tienda == "3":
            print("\n--- TIENDA VALORANT ---")
            print(
                "(1) Skin 1 --- 1300 Monedas \n(2) Skin 2 --- 740 Monedas \n(3) Skin 3 --- 2300 Monedas\n(4) Volver al menú principal")
            seleccion_compra = input("Seleccione que desea comprar: ")

            if seleccion_compra == "1":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 1300:
                    salario_total -= 1300
                    Lista_comseticos_Valorant.append("Skin 1 Valorant ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "2":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 740:
                    salario_total -= 740
                    Lista_comseticos_Valorant.append("Skin 2 Valorant ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "3":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 2300:
                    salario_total -= 2300
                    Lista_comseticos_Valorant.append("Skin 3 Valorant ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "4":
                seleccion_de_tienda = ""

        # --- SECCIÓN 4: TIENDA 2XKO ---
        while seleccion_de_tienda == "4":
            print("\n--- TIENDA 2XKO ---")
            print("(1) Chromas Pack --- 500 Monedas \n(2) Anunciador --- 900 Monedas \n(3) Volver al menú principal")
            seleccion_compra = input("Seleccione que desea comprar: ")

            if seleccion_compra == "1":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 500:
                    salario_total -= 500
                    Lista_comseticos_2XKO.append("Chromas Pack 2XKO ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "2":
                ingreso_usuario = input("Ingrese su usuario: ")
                if usuario == ingreso_usuario and salario_total >= 900:
                    salario_total -= 900
                    Lista_comseticos_2XKO.append("Anunciador 2XKO ")
                    print(f"¡El cosmético se ha enviado a su cuenta! Saldo restante: {salario_total}")
                else:
                    print("Error: Usuario incorrecto o saldo insuficiente.")
                seleccion_de_tienda = ""
            elif seleccion_compra == "3":
                seleccion_de_tienda = ""

    print("\n¡Gracias por usar la tienda de Riot! Saliendo...")
    lista_a_revisar_LOL.append(Lista_comseticos_LOL)
    lista_a_revisar_Valorant.append(Lista_comseticos_Valorant)
    lista_a_revisar_2xko.append(Lista_comseticos_2XKO)
    with open("Lista_Lol.txt", "a") as f:
        f.write( "\n"+usuario + "\n")
        f.writelines(Lista_comseticos_LOL)
    with open("Lista_Valorant.txt", "a") as f:
        f.write(usuario + "\n")
        f.writelines(Lista_comseticos_Valorant)
    with open("Lista_2xKo.txt", "a") as f:
        f.write(usuario + "\n")
        f.writelines(Lista_comseticos_2XKO)
    return usuario, salario_total, lista_a_revisar_Valorant, lista_a_revisar_LOL, lista_a_revisar_2xko


if __name__ == "__main__":
    ejecutar_tienda()
