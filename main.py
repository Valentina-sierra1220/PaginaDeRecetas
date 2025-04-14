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
app.route('/')(inicio.inicio)
app.route('/login', methods=['POST'])(inicio.login)


#clase para manejar las recetas
class Receta:
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos

    def obtener_ingredientes(self):
        return self.ingredientes

recetas_disponibles = [
    Receta("Ensalada", ["lechuga", "tomate", "zanahoria"], ["Lavar", "Cortar", "Mezclar"]),
    Receta("Tortilla", ["huevo", "papas", "sal"], ["Pelar", "Freír", "Batir"]),
    Receta("Sopa", ["agua", "pollo", "sal", "zanahoria"], ["Hervir", "Cocinar"]),
]

class Buscador:
    def buscar(self):
        termino = request.form['busqueda'].lower()  #lo que escribió el usuario
        resultados = []
        for receta in self.recetas:



if __name__ == '__main__':
    app.run(debug=True)



