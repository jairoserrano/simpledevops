from app import db

class Pets(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    color = db.Column(db.String(30))
    pet = db.Column(db.String(10))

    def __init__(self, name, color, pet):
        self.name = name
        self.color = color
        self.pet = pet

    def __repr__(self):
        return '<id {}>'.format(self.id)
