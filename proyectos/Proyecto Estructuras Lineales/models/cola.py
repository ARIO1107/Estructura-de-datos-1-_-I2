from datetime import datetime

# Clase que representa una tarea
class Tarea:
    def __init__(self, nombre, importancia , detalle=""):
        self.nombre = nombre
        self.importancia = importancia  # Alta, Media, Baja
        self.fecha = datetime.now().strftime("%d/%m/%Y %H:%M")  # Fecha de creación
        self.detalle = detalle
        self.finalizada = False  # Por defecto, no está finalizada

    def marcar_finalizada(self):
        self.finalizada = True

# Clase Cola para manejar las tareas
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar(self, tarea):
        self.items.append(tarea)

    def eliminar_por_indice(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def obtener_todas(self):
        return self.items

    def obtener(self, index):
        return self.items[index]
    
    def marcar_finalizada(self, index):    
        """Marca una tarea como finalizada por su posición en la cola."""
        if 0 <= index < len(self.items):
            self.items[index].marcar_finalizada()
