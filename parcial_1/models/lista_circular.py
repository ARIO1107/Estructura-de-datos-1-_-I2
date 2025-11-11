class Nodo:
    def __init__(self, figura, color):
        self.figura = figura
        self.color = color
        self.siguiente = None
        self.anterior = None


class ListaCircular:
    def __init__(self):
        self.actual = None
        self.figuras = ["Círculo", "Triángulo", "Cuadrado"]
        self.colores = ["rojo", "verde", "azul"]
        self.indice_color = 0
        self._crear_lista()

    def _crear_lista(self):
        nodos = [Nodo(f, self.colores[i]) for i, f in enumerate(self.figuras)]
        for i in range(len(nodos)):
            nodos[i].siguiente = nodos[(i + 1) % len(nodos)]
            nodos[i].anterior = nodos[(i - 1) % len(nodos)]
        self.actual = nodos[0]

    def avanzar(self):
        if self.actual:
            self.actual = self.actual.siguiente
            if self.actual.figura == "Círculo":
                self._rotar_colores()

    def retroceder(self):
        if self.actual:
            self.actual = self.actual.anterior
            if self.actual.figura == "Cuadrado":
                self._rotar_colores(-1)

    def _rotar_colores(self, direccion=1):
        # dirección=1 rota adelante, -1 rota atrás
        self.indice_color = (self.indice_color + direccion) % len(self.colores)
        colores_rotados = self.colores[self.indice_color:] + self.colores[:self.indice_color]

        nodo = self.actual
        for color in colores_rotados:
            nodo.color = color
            nodo = nodo.siguiente
