from flask_login import unicode

from project import db
from project import bcrypt

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255))
    emailFb = db.Column(db.String(255), nullable=True)
    emailTw = db.Column(db.String(255), nullable=True)
    idFb = db.Column(db.Integer)
    idTw = db.Column(db.Integer)

    def __init__(self, name, email, password, emailFb, emailTw, idFb, idTw):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.emailFb = emailFb
        self.emailTw = emailTw
        self.idFb = idFb
        self.idTw = idTw

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)
