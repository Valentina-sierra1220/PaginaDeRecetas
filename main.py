#para ejecutar
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('pagina.html')


if __name__ == '__main__':
    app.run(debug=True)




#Desde aqui la logica de la pagina de recetas

