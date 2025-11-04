class Nodo:
    def __init__(self, figura, color):
        self.figura = figura
        self.color = color
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        # Creamos los nodos en una lista para manejar rotación de colores
        self.nodos = [
            Nodo("Círculo", "rojo"),
            Nodo("Triángulo", "verde"),
            Nodo("Cuadrado", "azul")
        ]

        # Enlazamos circularmente
        for i in range(len(self.nodos)):
            self.nodos[i].siguiente = self.nodos[(i+1) % len(self.nodos)]

        # Nodo actual
        self.actual = self.nodos[0]

        # Colores para rotar
        self.colores = ["rojo", "verde", "azul"]
        self.indice_color = 0

    def avanzar(self):
        self.actual = self.actual.siguiente

    def retroceder(self):
        # Para retroceder, buscamos el nodo anterior
        temp = self.actual
        while temp.siguiente != self.actual:
            temp = temp.siguiente
        self.actual = temp

    def rotar_colores(self):
        # Rota los colores una posición
        self.indice_color = (self.indice_color + 1) % len(self.colores)
        colores_rotados = self.colores[self.indice_color:] + self.colores[:self.indice_color]
        for nodo, color in zip(self.nodos, colores_rotados):
            nodo.color = color

    def obtener_actual(self):
        return self.actual.figura, self.actual.color
