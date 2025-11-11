class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0


# -------------------------------
# Funciones auxiliares
# -------------------------------
def prioridad(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return 0


def infija_a_prefija(expresion):
    operadores = Pila()
    salida = []

    expresion = expresion[::-1]

    for c in expresion:
        if c.isdigit():
            salida.append(c)
        elif c == ')':
            operadores.push(c)
        elif c == '(':
            while not operadores.esta_vacia() and operadores.cima() != ')':
                salida.append(operadores.pop())
            operadores.pop()
        else:
            while (not operadores.esta_vacia() and
                   prioridad(c) < prioridad(operadores.cima())):
                salida.append(operadores.pop())
            operadores.push(c)

    while not operadores.esta_vacia():
        salida.append(operadores.pop())

    return ''.join(salida[::-1])


def evaluar_expresion(expresion):
    numeros = Pila()
    operadores = Pila()
    tokens = expresion.split()

    for t in tokens:
        if t.isdigit():
            numeros.push(int(t))
        elif t in "+-*/":
            operadores.push(t)

    while not operadores.esta_vacia():
        op = operadores.pop()
        b = numeros.pop()
        a = numeros.pop()

        if op == '+':
            r = a + b
        elif op == '-':
            r = a - b
        elif op == '*':
            r = a * b
        elif op == '/':
            r = a / b

        numeros.push(r)

    return numeros.pop()
