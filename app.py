from flask import Flask, escape, request, render_template, url_for # Importar la libreria

app = Flask(__name__) # Inicializamos la app con el nombre 

@app.route('/') #Definimos que la ruta de inicio será aplicadala funcion hola
def hola():
    return 'Hi Penguins!' # retorna Hi Penguins!


@app.route('/coach') # Creamos la ruta coach
def hola_coaches(): # Definimos la funcion que sera devuelta
    nombre = 'Karen' # Inicializamos un dato
    devolver = request.args.get('nombre',nombre) # Definimos que sera devuelto y renderizamos
    return f'hola, {escape(devolver)} '  # Retornamos al html

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


app.run(debug=True) # Para ejecutar