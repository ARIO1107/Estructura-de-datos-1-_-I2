# Representacio estatica - Lista de Contactos

# Estructura estática: una lista de diccionarios
contactos = [
    {"nombre": "Ana", "telefono": "76543210"},
    {"nombre": "Luis", "telefono": "70123456"},
    {"nombre": "Jose", "telefono": "78643517"},
    {"nombre": "Laura", "telefono": "7345546"}
]

# Mostrar todos los contactos
print("=== Lista de Contactos ===")
for c in contactos:
    print(f"Nombre: {c['nombre']} | Teléfono: {c['telefono']}")


def buscar_contacto():
    """Permite buscar un contacto por nombre las veces que el usuario quiera."""
    while True:
        busqueda = input("\nIngrese un nombre para buscar (o escriba 'salir' para terminar): ")

        if busqueda.lower() == "salir":
            print("👋 Saliendo del buscador de contactos...")
            break

        encontrado = False
        for c in contactos:
            if c["nombre"].lower() == busqueda.lower():
                print(f"📌 Contacto encontrado: {c['nombre']} - {c['telefono']}")
                encontrado = True

        if not encontrado:
            print("❌ Contacto no encontrado.")
            
buscar_contacto()