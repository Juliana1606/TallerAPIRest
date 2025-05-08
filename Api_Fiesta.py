from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configura la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Natachita.16@localhost/fiestas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de la tabla de tarjetas
class Tarjeta(db.Model):
    __tablename__ = 'info_tarjetas'  # Especifica el nombre de la tabla

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(5000), nullable=False)
    enlace = db.Column(db.String(300), nullable=True)

# Ruta de inicio para cargar la página HTML
@app.route('/')
def index():
    return render_template('Main.html')

# Ruta para obtener las tarjetas de la base de datos
@app.route('/api/info_tarjetas', methods=['GET'])
def obtener_tarjetas():
    try:
        # Obtener todas las tarjetas desde la base de datos
        tarjetas = Tarjeta.query.all()
        tarjetas_list = []

        for tarjeta in tarjetas:
            tarjeta_dict = {
                'id': tarjeta.id,
                'titulo': tarjeta.titulo,
                'descripcion': tarjeta.descripcion,
                'enlace': tarjeta.enlace
            }
            tarjetas_list.append(tarjeta_dict)

        return jsonify(tarjetas_list)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para agregar una nueva tarjeta (POST)
@app.route('/api/info_tarjetas', methods=['POST'])
def agregar_tarjeta():
    try:
        # Obtener los datos enviados por el usuario (JSON)
        data = request.get_json()

        # Crear una nueva tarjeta
        nueva_tarjeta = Tarjeta(
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            enlace=data.get('enlace')  # Enlace es opcional
        )

        # Agregar la tarjeta a la base de datos
        db.session.add(nueva_tarjeta)
        db.session.commit()

        return jsonify({"mensaje": "Tarjeta agregada con éxito"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para eliminar una tarjeta (DELETE)
@app.route('/api/info_tarjetas/<int:id>', methods=['DELETE'])
def eliminar_tarjeta(id):
    try:
        tarjeta = Tarjeta.query.get(id)
        if not tarjeta:
            return jsonify({"mensaje": "Tarjeta no encontrada"}), 404

        db.session.delete(tarjeta)
        db.session.commit()

        return jsonify({"mensaje": "Tarjeta eliminada con éxito"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
