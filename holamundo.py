from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo..!'

#metodos http    

@app.route('/lala/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return  'el id es ... ' + post_id
    else:
        return  'el id es no get ' + post_id


    return 'lala....'

@app.route('/lele')
def lele():
    return render_template('test.html')

