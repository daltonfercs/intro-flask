from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo..!'

@app.route('/lala')
def lala():
    return 'lala....'

@app.route('/lele')
def lele():
    return 'lele....'


