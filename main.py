from flask import Flask, render_template, request

app = Flask(__name__)

#desde aqui la logica

class Sesion:
    def inicio(self):
        return render_template('inicio.html')

    def login(self):
        usuario = request.form['usuario']
        correo = request.form['correo']
        return render_template('pagina.html', usuario=usuario, correo=correo)


sesion = Sesion()
app.route('/')(sesion.inicio)
app.route('/login', methods=['POST'])(sesion.login)

if __name__ == '__main__':
    app.run(debug=True)



