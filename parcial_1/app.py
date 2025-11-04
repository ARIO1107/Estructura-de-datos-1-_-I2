from flask import Flask, render_template, redirect, url_for
from models.lista_circular import ListaCircular

app = Flask(__name__)
lista = ListaCircular()
pasos = 0

@app.route('/')
def index():
    figura, color = lista.obtener_actual()
    return render_template('index.html', figura=figura, color=color)

@app.route('/avanzar')
def avanzar():
    global pasos
    lista.avanzar()
    pasos += 1
    if pasos % 3 == 0:
        lista.rotar_colores()
    return redirect(url_for('index'))

@app.route('/retroceder')
def retroceder():
    global pasos
    lista.retroceder()
    pasos += 1
    if pasos % 3 == 0:
        lista.rotar_colores()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
