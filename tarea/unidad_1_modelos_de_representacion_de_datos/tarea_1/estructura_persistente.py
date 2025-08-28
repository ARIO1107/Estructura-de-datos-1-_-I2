# Archivo donde se guardarán los contactos
archivo = "contactos.txt"

# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    with open(archivo, "a") as f:  # "a" = append (agregar al final)
        f.write(nombre + "," + telefono + "\n")
    print(f"Contacto agregado: {nombre} - {telefono}")

# Función para mostrar todos los contactos
def mostrar_contactos():
    print("Lista de contactos:")
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            for linea in lineas:
                nombre, telefono = linea.strip().split(",")
                print(nombre, "-", telefono)
    except FileNotFoundError:
        print("No hay contactos guardados aún.")

# Función para eliminar un contacto por nombre
def eliminar_contacto(nombre_borrar):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:  # "w" = escribir desde cero
            encontrado = False
            for linea in lineas:
                nombre, telefono = linea.strip().split(",")
                if nombre != nombre_borrar:
                    f.write(nombre + "," + telefono + "\n")
                else:
                    encontrado = True
            if encontrado:
                print(f"Contacto {nombre_borrar} eliminado.")
            else:
                print(f"No se encontró el contacto {nombre_borrar}.")
    except FileNotFoundError:
        print("No hay contactos guardados aún.")

# --- Ejemplo de uso ---
agregar_contacto("jose", "72345678")
agregar_contacto("sofia", "77654321")
agregar_contacto("maria", "69391658")
mostrar_contactos()
eliminar_contacto("jose")
mostrar_contactos()