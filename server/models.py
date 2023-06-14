from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


from flask_migrate import Migrate
# from models import db 

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    animals = db.relationship('Animal', back_populates='zookeeper')

class Enclosure(db.Model):

    __tablename__ = 'enclosures'
    __table_args__= (
        db.CheckConstraint("environment IN (\'Grass\', \'Sand\', \'Water\')", 
        name="env_check"),
    )
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String, nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    animals = db.relationship('Animal', back_populates='enclosure')


class Animal(db.Model):
    __tablename__ = 'animals'
    # __tableargs__= primary key constraints foreign key constraints etc
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    species = db.Column(db.String, nullable=False)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"))
    enclosure = db.Column(db.Integer, db.ForeignKey("enclosures.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # ask question about cascading
    zookeeper = db.relationship("Zookeeper", back_populates = 'animals')
    enclosure = db.relationship("Zookeeper", back_populates = 'animals')

def __repr__(self):
    return f"<Animal #{self.id}:\n"\
    +f"Name: {self.name}"\
    +f"Species: {self.species}"