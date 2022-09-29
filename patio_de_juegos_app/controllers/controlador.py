from patio_de_juegos_app import app
from flask import render_template

@app.route('/')
def plantilla():
    return 'Patio de juegos'

@app.route('/play')
def plantilla_1():
    return render_template('index.html', color = 'lightblue', veces=3)

@app.route('/play/<int:numero>/<string:color>')
def plantilla_2(numero, color):
    return render_template("index.html", veces=numero, color=color)


