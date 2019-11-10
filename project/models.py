from project import db
from project.utils import Utils


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email_fb = db.Column(db.String(255))
    email_tw = db.Column(db.String(255))
    id_fb = db.Column(db.String(255))
    id_tw = db.Column(db.String(255))

    def __init__(self, email, password=None, email_fb=None, email_tw=None, id_fb=None, id_tw=None):
        self.email = email
        self.password = Utils.hash_password(password)
        self.email_fb = email_fb
        self.email_tw = email_tw
        self.id_fb = id_fb
        self.id_tw = id_tw

    def __repr__(self):
        return '<email - {}>'.format(self.email)