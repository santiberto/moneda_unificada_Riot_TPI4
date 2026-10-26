def buscar_usuario_en_archivo(nombre_archivo, usuario_buscado):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            encontrado = False
            lineas_mostradas = 0

            print(f"\n--- Buscando información para el usuario: '{usuario_buscado}' ---")

            for linea in archivo:
                linea_limpia = linea.strip()

                # Si encontramos la línea que coincide con el usuario buscado
                if linea_limpia.lower() == usuario_buscado.lower():
                    encontrado = True
                    print(f"\n[Usuario encontrado: {linea_limpia}]")
                    continue  # Pasamos a la siguiente línea para empezar a mostrar datos

                # Si ya estamos dentro del bloque del usuario, mostramos sus datos
                if encontrado:
                    # Condición para detenernos si encontramos el *próximo* usuario
                    # (Asumimos que un nuevo usuario no tiene espacios o cumple un formato de cabecera,
                    # o simplemente si la línea no está vacía y marca el inicio de otro registro).
                    # *Nota: Puedes ajustar esta condición según cómo esté estructurado tu .txt*
                    if linea_limpia.startswith("Usuario:") or (linea_limpia != "" and not linea_limpia.startswith("-")):
                        # Si tu archivo tiene separadores claros para el siguiente usuario, descomenta la línea de abajo:
                        # break
                        pass

                    # Mostramos la línea actual del archivo
                    print(linea_limpia)
                    lineas_mostradas += 1

                    # Opcional: si quieres frenar exactamente en la siguiente línea que parezca un nuevo usuario,
                    # puedes usar una marca. Por ahora mostrará todo hasta el final o hasta encontrar otra coincidencia clara.

            if not encontrado:
                print(f"Lo sentimos, el usuario '{usuario_buscado}' no fue encontrado en el archivo.")
            elif lineas_mostradas == 0:
                print("El usuario existe pero no tiene registros asociados debajo.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Asegúrate de crearlo primero.")


# --- Programa Principal ---
if __name__ == "__main__":
    # Nombre del archivo de texto de ejemplo
    archivo_txt = "usuarios_datos.txt"

    # Solicitamos el usuario por teclado
    usuario_ingresado = input("Ingrese su nombre de usuario: ").strip()

    # Ejecutamos la búsqueda
    buscar_usuario_en_archivo("Lista_2XKO.txt", usuario_ingresado)