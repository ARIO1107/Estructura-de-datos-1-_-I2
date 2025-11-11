from flask import Flask, render_template, redirect, url_for
from models.lista_circular import ListaCircular

app = Flask(__name__)

lista = ListaCircular()

@app.route('/')
def index():
    return render_template(
        'index.html',
        figura=lista.actual.figura,
        color=lista.actual.color
    )

@app.route('/avanzar')
def avanzar():
    lista.avanzar()
    return redirect(url_for('index'))

@app.route('/retroceder')
def retroceder():
    lista.retroceder()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True , port = 5020)
