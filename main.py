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
        return render_template('principal.html', usuario=usuario)






#clase para manejar las recetas
class Receta:
    def __init__(self, nombre, ingredientes, pasos, imagen):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos
        self.imagen = imagen

    def obtener_ingredientes(self):
        return self.ingredientes



class Buscador:
    def __init__(self, recetas):
        self.recetas = recetas

    def buscar_por_ingrediente(self, termino):
        resultados = []
        terminos = [t.strip() for t in termino.split(',')]
        for receta in self.recetas:
            for ingrediente in receta.obtener_ingredientes():
                for t in terminos:
                    if t in ingrediente.lower():
                        resultados.append(receta)
                        break
                else:
                    continue
                break
        return resultados


class AdministradorRecetas:
    def __init__(self):
        self.recetas = [
            Receta("Ensalada", ["lechuga", "tomate", "zanahoria"], ["Lavar", "Cortar", "Mezclar"],"salsas.jpg"),
            Receta("Tortilla", ["huevo", "papas", "sal"], ["Pelar", "Freír", "Batir"],"salsas.jpg"),
            Receta("Sopa", ["agua", "pollo", "sal", "zanahoria"], ["Hervir", "Cocinar"], "salsas.jpg"),
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
        app.route('/batidos')(self.mostrar_batidos)
        app.route('/postres')(self.mostrar_postres)
        app.route('/salsas')(self.mostrar_salsas)
        app.route('/pizzas')(self.mostrar_pizzas)
        app.route('/pastas')(self.mostrar_pastas)
        app.route('/hamburguesas')(self.mostrar_hamburguesas)
        app.route('/fitness')(self.mostrar_fitness)
        app.route('/mexicano')(self.mostrar_mexicanos)
        app.route('/desayunos')(self.mostrar_desayunos)

    def buscar(self):
        termino = request.form['busqueda'].lower()
        resultados = self.administrador.obtener_resultados_busqueda(termino)
        return render_template('pagina.html', usuario="Invitado", recetas=resultados, busqueda_realizada=True)


#en la pagina principal la parte de inspirarme
    def mostrar_batidos(self):
        return render_template('batidos.html')

    def mostrar_postres(self):
        return render_template('postres.html')

    def mostrar_salsas(self):
        return render_template('salsas.html')

    def mostrar_pizzas(self):
        return render_template('pizzas.html')

    def mostrar_pastas(self):
        return render_template('pastas.html')

    def mostrar_hamburguesas(self):
        return render_template('hamburguesas.html')

    def mostrar_fitness(self):
        return render_template('fitness.html')

    def mostrar_mexicanos(self):
        return render_template('mexicano.html')

    def mostrar_desayunos(self):
        return render_template('desayunos.html')
controlador = Controlador()
controlador.configurar_rutas()




if __name__ == '__main__':
    app.run(debug=True)



