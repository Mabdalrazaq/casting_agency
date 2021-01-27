import os
import unittest
import json
from models import setup_db, Actor,Movie
from app import create_app

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path=os.environ['HEROKU_POSTGRESQL_MAUVE_URL']
        self.casting_assistant_token=os.environ['CASTING_ASSISTANT_TOKEN']
        self.casting_director_token=os.environ['CASTING_DIRECTOR_TOKEN']
        self.executive_producer_token=os.environ['EXECUTIVE_DIRECTOR_TOKEN']
        self.db=setup_db(self.app,database_path=self.database_path)

        self.new_movie={
            "title":"new_title",
            "release_date":"1999/1/1"
        }

        self.new_actor={
            "name":"new_actor",
            "age":0,
            "gender":"male"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()
            movie=Movie("title","1999/1/1")
            movie.add()
            actor=Actor("name",0,"gender")
            actor.add()
            
    
    def tearDown(self):
        pass

    def test_retrieve_movies(self):
        res=self.client().get('/movies',
        headers={"Authorization":"Bearer "+self.casting_assistant_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['movies']))

    def test_error_retrieve_movies_without_authorization(self):
        res=self.client().get('/movies')
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)

    def test_retrieve_actors(self):
        res=self.client().get('/actors',
        headers={"Authorization":"Bearer "+self.casting_assistant_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['actors']))

    def test_error_retrieve_actors_without_authorization(self):
        res=self.client().get('/actors')
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)


    def test_create_movie(self):
        res=self.client().post('/movies',json=self.new_movie,
        headers={"Authorization":"Bearer "+self.executive_producer_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_create_movie_without_authorization(self):
        res=self.client().post('/movies',json=self.new_movie)
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)

    def test_create_actor(self):
        res=self.client().post('/actors',json=self.new_actor,
        headers={"Authorization":"Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_create_actor_without_authorization(self):
        res=self.client().post('/actors',json=self.new_actor)
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)

    def test_edit_movie(self):
        res=self.client().patch('/movies/1',json={"title":"new_title"},
        headers={"Authorization": "Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_edit_unexisting_movie(self):
        res=self.client().patch('/movies/1000',json={"title":"new_title"},
        headers={"Authorization": "Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)

    def test_edit_actor(self):
        res=self.client().patch('/actors/1',json={"name":"new_name"},
        headers={"Authorization": "Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_edit_unexisting_actor(self):
        res=self.client().patch('/actors/1000',json={"name":"new_name"},
        headers={"Authorization": "Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)



    def test_delete_movie(self):
        res=self.client().delete('/movies/1',
        headers={"Authorization":"Bearer "+self.executive_producer_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_delete_unexisting_movie(self):
        res=self.client().delete('/movies/1000',
        headers={"Authorization":"Bearer "+self.executive_producer_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)

    def test_delete_actor(self):
        res=self.client().delete('/actors/1',
        headers={"Authorization":"Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_delete_unexisting_actor(self):
        res=self.client().delete('/actors/1000',
        headers={"Authorization":"Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)






    def test_casting_assistant_reads_movies(self):
        res=self.client().get('/movies',
        headers={"Authorization":"Bearer "+self.casting_assistant_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_casting_assistant_cannot_create_actor(self):
        res=self.client().post('/actors',json=self.new_actor,
        headers={"Authorization": "Bearer "+self.casting_assistant_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)

    def test_casting_director_creates_actor(self):
        res=self.client().post('/actors',json=self.new_actor,
        headers={"Authorization":"Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_error_casting_assistant_cannot_create_movie(self):
        res=self.client().post('/movies',json=self.new_movie,
        headers={"Authorization": "Bearer "+self.casting_director_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)

    def test_executive_producer_creates_movie(self):
        res=self.client().post('/movies',json=self.new_movie,
        headers={"Authorization":"Bearer "+self.executive_producer_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_executive_producer_creates_actor(self):
        res=self.client().post('/actors',json=self.new_actor,
        headers={"Authorization":"Bearer "+self.executive_producer_token})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)







# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()