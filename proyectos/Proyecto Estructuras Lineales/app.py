from flask import Flask, render_template, request, redirect, url_for
from models.cola import Cola

app = Flask(__name__)

# Instanciamos una sola cola (modelo)
cola_tareas = Cola()


@app.route('/')
def index():
    tareas = cola_tareas.obtener_todos()
    return render_template('index.html', tareas=tareas)


@app.route('/agregar', methods=['POST'])
def agregar():
    tarea = request.form['tarea']
    if tarea.strip():
        cola_tareas.encolar(tarea)
    return redirect(url_for('index'))


@app.route('/quitar', methods=['POST'])
def quitar():
    cola_tareas.desencolar()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)