from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Date

database_path='postgresql://postgres:postgres@localhost:5432/agency'
db=SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app=app
    db.init_app(app)
    return db

class Movie(db.Model):
    __tablename__ = 'movie'
    id =Column(Integer, primary_key=True)
    title=Column(String)
    release_date=Column(Date)


class Artist(db.Model):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name=Column(String)
    age=Column(Integer)
    gender=Column(String)

