from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.DECIMAL(precision=10, scale=2), nullable=False)

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': str(self.price)  # Convert decimal to string for JSON serialization
        }
