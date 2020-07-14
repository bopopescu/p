from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://sql3354595:7Haz6Ng1fm@sql3.freemysqlhosting.net/sql3354595'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)


class TipoUsuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    texto = db.Column(db.String(50))

    usuarios = db.relationship('Usuarios', backref='tipo', lazy='dynamic')

    def __init__(self, texto):
        self.texto = texto


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    usuario = db.Column(db.String(50))
    externa = db.Column(db.Integer, db.ForeignKey('tipo_usuarios.id'))

    def __init__(self, usuario):
        self.usuario = usuario


@app.route('/')
def index():
    return 'Hola'


@app.route('/prueba')
def prueba():
    us = Usuarios.query.all()
    return render_template('db.html', us=us)


if __name__ == "__main__":
    app.run(debug=True)
