from app import db

from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.Text)
    email = db.Column(db.String(100))
    no_hp = db.Column(db.String(16))

    def __init__(self, full_name, username, password, email, no_hp):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
        self.no_hp = no_hp

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)
