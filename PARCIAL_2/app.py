from flask import Flask, render_template, request
from models.pilas import Pila, infija_a_prefija, evaluar_expresion

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    prefija = ""
    expresion_infija = ""
    numeros_lista = []
    operadores_lista = []

    if request.method == 'POST':
        # Entrada en notación infija normal
        entrada = request.form['entrada']

        # Separar tokens por espacio
        tokens = entrada.split()

        # Llenar pilas de números y operadores
        pila_num = Pila()
        pila_op = Pila()

        for t in tokens:
            if t.isdigit():
                pila_num.push(t)
            elif t in "+-*/":
                pila_op.push(t)

        # Reconstruir la expresión infija usando pop de pilas
        try:
            # Comenzamos con el primer número
            expresion_infija = pila_num.items[0]
            index_num = 1
            index_op = 0

            while index_op < len(pila_op.items):
                op = pila_op.items[index_op]
                num = pila_num.items[index_num]
                expresion_infija = f"{expresion_infija} {op} {num}"
                index_op += 1
                index_num += 1

            # Convertir a prefija y calcular resultado
            prefija = infija_a_prefija(expresion_infija.replace(" ", ""))
            resultado = evaluar_expresion(expresion_infija)

            # Guardar listas para mostrar
            numeros_lista = pila_num.items
            operadores_lista = pila_op.items

        except Exception:
            resultado = "❌ Error al calcular"

    return render_template('index.html',
                           entrada=entrada if request.method=='POST' else '',
                           numeros=numeros_lista,
                           operadores=operadores_lista,
                           expresion=expresion_infija,
                           prefija=prefija,
                           resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
