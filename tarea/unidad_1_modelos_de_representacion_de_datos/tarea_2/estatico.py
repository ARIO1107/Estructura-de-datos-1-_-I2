# Clase Automovil con estructura estática
class AutomovilEstatico:
    MAX_MANTENIMIENTOS = 5  # Máximo de registros

    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.historial_mantenimientos = [None] * self.MAX_MANTENIMIENTOS
        self.contador = 0

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
        if self.contador < self.MAX_MANTENIMIENTOS:
            self.historial_mantenimientos[self.contador] = {"fecha": fecha, "descripcion": descripcion}
            self.contador += 1
        else:
            print("No se pueden agregar más mantenimientos (límite alcanzado).")

    # Método para mostrar historial
    def mostrar_historial(self):
        print(f"Historial de {self.marca} {self.modelo}:")
        for m in self.historial_mantenimientos:
            if m is not None:
                print(f"- {m['fecha']}: {m['descripcion']}")

# --- Ejemplo de uso ---
auto2 = AutomovilEstatico("Honda", "Civic", "Azul", 2022)
auto2.agregar_mantenimiento("2025-08-28", "Cambio de aceite")
auto2.agregar_mantenimiento("2025-08-30", "Revisión de frenos")
auto2.mostrar_historial()