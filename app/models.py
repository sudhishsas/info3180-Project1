from . import db

class PropertiesProfie(db.Model):

    __tablename__ = 'properties_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180),nullable=False)
    location = db.Column(db.String(280),nullable=False)
    num_bath = db.Column(db.Integer,nullable=False)
    num_bed = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    photo= db.Column(db.String(200),nullable=False)
    type = db.Column(db.String(15),nullable=False)


    def __init__(self, type ,id, title, location, num_bath, num_bed, price,photo):
        self.title = title 
        self.location = location
        self.num_bath = num_bath
        self.num_bed = num_bed
        self.price = price  
        self.id = id
        self.photo = photo
        self.type = type

