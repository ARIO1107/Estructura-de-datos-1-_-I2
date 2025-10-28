class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if not self.frente:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if not self.frente:
            return None
        valor = self.frente.dato
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        return valor

    def obtener_todos(self):
        actual = self.frente
        datos = []
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos
