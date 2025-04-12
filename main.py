from flask import Flask, render_template, request

app = Flask(__name__)

#desde aqui la logica


#clase de formulario de inicio de sesión
class InicioSesion:
    def inicio(self):
        return render_template('index.html')

    def login(self):
        usuario = request.form['usuario']
        correo = request.form['correo']
        return render_template('pagina.html', usuario=usuario, correo=correo)


inicio = InicioSesion()
app.route('/')(sesion.inicio)
app.route('/login', methods=['POST'])(sesion.login)


#clase para manejar las recetas
class Receta:
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos

if __name__ == '__main__':
    app.run(debug=True)



