from flask import Flask, render_template, request, redirect, url_for
from models.cola import Cola, Tarea

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Evita caché

cola_tareas = Cola()

@app.route('/')
def index():
    importancia_orden = {"Alta": 3, "Media": 2, "Baja": 1}
    tareas = sorted(cola_tareas.obtener_todas(),
                    key=lambda t: importancia_orden[t.importancia],
                    reverse=True)
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    importancia = request.form['importancia']
    detalle = request.form.get('detalle', '').strip()  #  si no hay detalle, será cadena vacía
    
    if nombre:
        tarea = Tarea(nombre, importancia, detalle)
        cola_tareas.agregar(tarea)
    return redirect(url_for('index'))

@app.route('/finalizar/<int:index>')
def finalizar(index):
    tarea = cola_tareas.obtener(index)
    tarea.marcar_finalizada()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:index>')
def eliminar(index):
    cola_tareas.eliminar_por_indice(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
