from flask_login import unicode

from project import db
from project import bcrypt

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email_fb = db.Column(db.String(255))
    email_tw = db.Column(db.String(255))
    id_fb = db.Column(db.String(255))
    id_tw = db.Column(db.String(255))

    def __init__(self, email, password, email_fb, email_tw, id_fb, id_tw):
        self.email = email
        self.password = "" if password == bytes("", "utf-8") else bcrypt.generate_password_hash(password)
        self.email_fb = email_fb
        self.email_tw = email_tw
        self.id_fb = id_fb
        self.id_tw = id_tw

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
