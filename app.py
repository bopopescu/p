from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://sql3354595:7Haz6Ng1fm@sql3.freemysqlhosting.net/sql3354595'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

class Prueba(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    texto = db.Column(db.String(50))

    us = db.relationship('Usuarios', backref='us', lazy='dynamic')

    def __init__(self,texto):
        self.texto = texto

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    usuario = db.Column(db.String(50))
    externa = db.Column(db.Integer, db.ForeignKey('prueba.id'))

    def __init__(self,usuario,externa):
        self.usuario = usuario

@app.route('/')
def index():
    return 'Hola'

if __name__ == "__main__":
    app.run(debug=True)