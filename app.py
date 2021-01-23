import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, Actor, Movie
from auth import requires_auth, AuthError

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


  @app.route('/movies')
  @requires_auth("get:movies")
  def get_movies(payload):
    movies=Movie.query.all()
    return jsonify({
      'success':True,
      'movies':[movie.format() for movie in movies]
    })

  @app.route('/actors')
  @requires_auth("get:actors")
  def get_actors(payload):
    actors=Actor.query.all()
    return jsonify({
      'success':True,
      'actors':[actor.format() for actor in actors]
    })

  @app.route('/movies',methods=["post"])
  @requires_auth("post:movies")
  def post_movies(payload):
    title=request.get_json().get('title','untitled')
    release_date=request.get_json().get('release_date',None)
    movie= Movie(title,release_date)
    movie.add()
    return jsonify({
      'success':True,
      'movie': movie.format()
    })

  @app.route('/actors',methods=["post"])
  @requires_auth("post:actors")
  def post_actors(payload):
    name=request.get_json().get('name','unknown')
    age=request.get_json().get('age',0)
    gender=request.get_json().get('gender','unknown')
    actor=Actor(name,age,gender)
    actor.add()
    return jsonify({
      'success':True,
      'actor': actor.format()
    })


  @app.route('/movies/<int:movie_id>',methods=["delete"])
  @requires_auth("delete:movies")
  def delete_movies(payload,movie_id):
    movie= Movie.query.filter_by(id=movie_id).one_or_none()
    if movie is None:
      abort(404)
    movie.delete()
    return jsonify({
      'success':True,
      'movie':movie.format()
    })

  @app.route('/actors/<int:actor_id>',methods=["delete"])
  @requires_auth("delete:actors")
  def delete_actors(payload,actor_id):
    actor= Actor.query.filter_by(id=actor_id).one_or_none()
    if actor is None:
      abort(404)
    actor.delete()
    return jsonify({
      'success':True,
      'actor':actor.format()
    })

  @app.route('/movies/<int:movie_id>',methods=["patch"])
  @requires_auth("patch:movies")
  def patch_movies(payload,movie_id):
    movie= Movie.query.filter_by(id=movie_id).one_or_none()
    if(movie is None):
      abort(404)
    title=request.get_json().get('title')
    release_date=request.get_json().get('release_date')
    movie.title=title if title!=None else movie.title
    movie.release_date=release_date if release_date!=None else movie.release_date
    movie.update()
    return jsonify({
      'success':True,
      'movie': movie.format()
    })

  @app.route('/actors/<int:actor_id>',methods=["patch"])
  @requires_auth("patch:actors")
  def patch_actors(payload,actor_id):
    actor= Actor.query.filter_by(id=actor_id).one_or_none()
    if(actor is None):
      abort(404)
    name=request.get_json().get('name')
    age=request.get_json().get('age')
    gender=request.get_json().get('gender')
    actor.name=name if name!=None else actor.name
    actor.age=age if age!=None else actor.age
    actor.gender=gender if gender!=None else actor.gender
    actor.update()
    return jsonify({
      'success':True,
      'actor':actor.format()
    })

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False, 
          "error": 422,
          "message": "Unprocessable"
      }), 422


  @app.errorhandler(404)
  def not_found(e):
      return jsonify({
          "success":False,
          "error":404,
          "message":"Not Found"
      }), 404

  @app.errorhandler(500)
  def internal_error(error):
    return jsonify({
      'success':False,
      'message':'internal server error',
      'error':500
    }),500


  @app.errorhandler(AuthError)
  def auth_error(e):
      return jsonify({
          "success":False,
          "error":e.status_code,
          "message": e.error.get('code')+": "+e.error.get('description')
      }), e.status_code

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)