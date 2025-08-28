# Lista para almacenar libros - simulando estructura
biblioteca = []

# Función para agregar un libro
def agregar_libro(titulo, autor, anio):
    libro = {"titulo": titulo, "autor": autor, "anio": anio}  # Simula la estructura
    biblioteca.append(libro)
    print(f"Libro agregado: {titulo} de {autor}, {anio}")

# Función para mostrar todos los libros
def mostrar_biblioteca():
    print("\nBiblioteca:")
    for l in biblioteca:
        print(f"- {l['titulo']} | {l['autor']} | {l['anio']}")

# Función para buscar libros por autor
def buscar_por_autor(autor):
    print(f"\nLibros de {autor}:")
    encontrados = False
    for l in biblioteca:
        if l["autor"] == autor:
            print(f"- {l['titulo']} ({l['anio']})")
            encontrados = True
    if not encontrados:
        print("No se encontraron libros de ese autor.")

# --- Ejemplo de uso ---
agregar_libro("1984", "George Orwell", 1949)
agregar_libro("Animal Farm", "George Orwell", 1945)
agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)

mostrar_biblioteca()
buscar_por_autor("George Orwell")
buscar_por_autor("Steven king")