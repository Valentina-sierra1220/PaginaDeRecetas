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
    def __init__(self, recetas):
        self.recetas = recetas

    def buscar_por_ingrediente(self, termino):
        resultados = []
        for receta in self.recetas:
            for ingrediente in receta.obtener_ingredientes():
                if termino in ingrediente.lower():
                    resultados.append(receta)
                    break
                return resultados


class AdministradorRecetas:
    def __init__(self):
        self.recetas = [
        Receta("Ensalada", ["lechuga", "tomate", "zanahoria"], ["Lavar", "Cortar", "Mezclar"]),
        Receta("Tortilla", ["huevo", "papas", "sal"], ["Pelar", "Freír", "Batir"]),
        Receta("Sopa", ["agua", "pollo", "sal", "zanahoria"], ["Hervir", "Cocinar"]),
    ]
    self.buscador = Buscador(self.recetas)

    def obtener_resultados_busqueda(self, termino):
        return self.buscador.buscar_por_ingrediente(termino)




class Controlador:
    def __init__(self):
        self.inicio = InicioSesion()
        self.administrador = AdministradorRecetas()

    def configurar_rutas(self):
        app.route('/')(self.inicio.inicio)
        app.route('/login', methods=['POST'])(self.inicio.login)
        app.route('/buscar', methods=['POST'])(self.buscar)

    def buscar(self):
        termino = request.form['busqueda'].lower()
        resultados = self.administrador.obtener_resultados_busqueda(termino)
        return render_template('pagina.html', usuario="Invitado", recetas=resultados)

controlador = Controlador()
controlador.configurar_rutas()




if __name__ == '__main__':
    app.run(debug=True)



