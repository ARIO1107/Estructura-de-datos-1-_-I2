# Representacio dinamica - Lista para guardar puntajes
def ejemplo_puntajes():
    print("\n--- Puntajes de Jugadores ---")
    puntajes = []

    def agregar_puntaje(nombre, puntos):
        puntajes.append([nombre, puntos])
        print(f"Puntaje agregado: {nombre} - {puntos} puntos")

    def mostrar_puntajes():
        print("Lista de puntajes:")
        for p in puntajes:
            print(p[0], "-", p[1], "puntos")

    def puntaje_total():
        total = 0
        for p in puntajes:
            total += p[1]
        print("Puntaje total de todos los jugadores:", total)

    # Ejemplo de uso
    agregar_puntaje("Ren", 10)
    agregar_puntaje("Lia", 15)
    agregar_puntaje("Kai", 8)
    mostrar_puntajes()
    puntaje_total()

ejemplo_puntajes()