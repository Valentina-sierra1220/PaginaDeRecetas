from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

favoritas = set()

class InicioSesion:
    def inicio(self):
        return render_template('index.html')

    def login(self):
        usuario = request.form['usuario']
        correo = request.form['correo']
        return render_template('principal.html', usuario=usuario)

class Receta:
    def __init__(self, nombre, ingredientes, pasos, cantidades, imagen):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos
        self.cantidades = cantidades
        self.imagen = imagen

    def obtener_ingredientes(self):
        return self.ingredientes

class Buscador:
    def __init__(self, recetas):
        self.recetas = recetas

    def buscar_por_ingrediente(self, termino):
        resultados = []
        terminos = [t.strip().lower() for t in termino.split(',')]
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
            Receta(
                "Torta De Chocolate",
                ["huevo", "mantequilla", "chocolate negro", "azúcar", "harina de trigo", "sal", "chocolate con leche",
                 "nata líquida"],
                [
                    "1. Precalienta el horno a 180°C.",
                    "2. Coloca el chocolate en tu procesador de alimentos y rállalo durante varios segundos.",
                    "3. Coloca 130 gramos de mantequilla cortada en trozos y el chocolate rallado en un cazo. Calienta a fuego suave hasta que el chocolate se funda.",
                    "4. Vierte el chocolate fundido en un recipiente y añade el azúcar y las yemas de huevo. Mezcla hasta integrar.",
                    "5. Añade la harina y mezcla hasta que no queden grumos.",
                    "6. Monta las claras a punto de nieve con una pizca de sal. Mézclalas con el chocolate con movimientos envolventes.",
                    "7. Engrasa un molde de unos 20 cm de diámetro y rellénalo con la mezcla. Hornea a 180°C durante 40 minutos con calor arriba y abajo.",
                    "8. Para la cobertura, vierte el chocolate con leche, la nata líquida y el resto de la mantequilla en un cazo. Calienta a fuego medio hasta que se derrita.",
                    "9. Esparce el chocolate por encima del bizcocho y deja que se enfríe. Decora al gusto."
                ],
                [
                    "Huevos: 6 unidades",
                    "Mantequilla: 150 gramos",
                    "Chocolate negro: 200 gramos",
                    "Azúcar: 150 gramos",
                    "Harina de trigo: 150 gramos",
                    "Sal: una pizca",
                    "Chocolate con leche: 100 gramos",
                    "Nata líquida: 100 ml"
                ],
                "tortaChocolate.jpg"
            )
        ]
        self.buscador = Buscador(self.recetas)

    def obtener_resultados_busqueda(self, termino):
        return self.buscador.buscar_por_ingrediente(termino)

class Controlador:
    def __init__(self):
        self.inicio = InicioSesion()
        self.administrador = AdministradorRecetas()
        self.recetas_creadas = []

    def configurar_rutas(self):
        app.route('/')(self.inicio.inicio)
        app.route('/login', methods=['POST'])(self.inicio.login)
        app.route('/buscar', methods=['POST'])(self.buscar)
        app.route('/guardar/<nombre_receta>', methods=['POST'])(self.guardar)
        app.route('/batidos')(self.mostrar_batidos)
        app.route('/postres')(self.mostrar_postres)
        app.route('/salsas')(self.mostrar_salsas)
        app.route('/pizzas')(self.mostrar_pizzas)
        app.route('/pastas')(self.mostrar_pastas)
        app.route('/hamburguesas')(self.mostrar_hamburguesas)
        app.route('/fitness')(self.mostrar_fitness)
        app.route('/mexicano')(self.mostrar_mexicanos)
        app.route('/desayunos')(self.mostrar_desayunos)
        app.route('/perfil')(self.mostrar_perfil)
        app.route('/enterate')(self.mostrar_enterate)
        app.route('/crear_receta', methods=['POST'])(self.crear_receta)

    def buscar(self):
        termino = request.form['busqueda'].lower()
        resultados = self.administrador.obtener_resultados_busqueda(termino)
        usuario = "Invitado"
        return render_template('pagina.html', usuario=usuario, recetas=resultados, busqueda_realizada=True,
                               favoritas=favoritas)

    def guardar(self, nombre_receta):
        if nombre_receta in favoritas:
            favoritas.remove(nombre_receta)
        else:
            favoritas.add(nombre_receta)
        return '', 204

    def crear_receta(self):
        titulo = request.form.get('titulo-receta', '').strip()
        descripcion = request.form.get('descripcion-receta', '').strip()
        if titulo:
            self.recetas_creadas.append({'titulo': titulo, 'descripcion': descripcion})
        return redirect(url_for('mostrar_perfil'))

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

    def mostrar_enterate(self):
        return render_template('enterate.html')

    def mostrar_perfil(self):
        receta_seleccionada = request.args.get('receta', None)
        receta_obj = None
        if receta_seleccionada:
            for r in self.recetas_creadas:
                if r['titulo'] == receta_seleccionada:
                    receta_obj = r
                    break
        return render_template('perfil.html', favoritas=favoritas,
                               recetas_creadas=self.recetas_creadas,
                               receta_mostrar=receta_obj)

controlador = Controlador()
controlador.configurar_rutas()

if __name__ == '__main__':
    app.run(debug=True)
