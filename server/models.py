from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# contains definitions of tables and associated schema constructs
# MetaData is a container object that keeps together many different features of a database (or multiple databases) being described.
metadata = MetaData()


# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)


# define a model class by inheriting from db.Model.
class Pet(db.Model):           #The Pet class is declared as a subclass of db.Model
    __tablename__ = 'pets'     #The database table is named pets.

    id = db.Column(db.Integer, primary_key=True)    #The database table has 3 columns: id, name & species
    name = db.Column(db.String)
    species = db.Column(db.String)
