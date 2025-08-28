# Clase Automovil con estructura dinámica
class AutomovilDinamico:
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.historial_mantenimientos = []  # Lista dinámica

    # Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_anio(self):
        return self.anio

    # Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_color(self, color):
        self.color = color

    def set_anio(self, anio):
        self.anio = anio

    # Método para agregar mantenimiento
    def agregar_mantenimiento(self, fecha, descripcion):
        self.historial_mantenimientos.append({"fecha": fecha, "descripcion": descripcion})

    # Método para mostrar historial
    def mostrar_historial(self):
        print(f"Historial de {self.marca} {self.modelo}:")
        for m in self.historial_mantenimientos:
            print(f"- {m['fecha']}: {m['descripcion']}")

# --- Ejemplo de uso ---
auto1 = AutomovilDinamico("Toyota", "Corolla", "Rojo", 2023)
auto1.agregar_mantenimiento("2025-08-28", "Cambio de aceite")
auto1.agregar_mantenimiento("2025-08-30", "Revisión de frenos")
auto1.mostrar_historial()