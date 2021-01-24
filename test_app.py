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
        self.casting_assistant_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzNkM2QzNDAyODUwMDcxNjAzNDIxIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE0MTQ4NzQsImV4cCI6MTYxMTUwMTI3NCwiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.GVkysbVVdU9tAtKJ_T5FIc-6LEeX6t3yL-scbG_V75Dwj6kFTMsA4FGJNbMR7HqBzyQ511CVOoPqAYcHbq-4ya_cMyeB39tpfE5YuyyO-Qo2okNJ3XcRFeloojuJUKRd5rl0pV2FancbJGO6trh__uHOtGQw0RxtyZqLBbiUBrdxTYSlGuRGCyldv61GtzUSyQA5R7Q73gfV-PJXLKZ-v9FjYsfIMLwVMzlmExPdCgXE8SLzAqFX5uThpDYiw1_jMaQqbFE6nVu_xfsLRX-kOckJBwGEYyZGXwIP7gH1s-TQc3kAqtPmnoXx7OGQIJt2dIbLbt-Kpyc1YquLOStq0g"
        self.casting_director_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzNjYmVmZmNiZTIwMDZhODg1ZmRiIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE0MTQ3NTUsImV4cCI6MTYxMTUwMTE1NSwiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.XaC4OO3TOzxSLrk3yDEvsigu0IyFD2OVXhG2HZ2TvKdIQ0T4ONTQTCRuMZoDUyQl9Kfy48h-ZLHDM0AR-K3yG3SdxqDPcuH1ha_Mh_2P2LPD0djZ6dAcH5ZzbldsgLvo82EcgH03gnePmkrGkE7MhB9dUhazZ-o4zYhhFvzQL8z0RwJoicBO3vwGl3T8n3rGrO-HX3i8d55OF9iOJH7xKKoNIwVTeTH4YSeLN0uxvUEuv6CLaMCkE9IU1hd6XlQ8e27ezchuxtNHZ07vO9bd1I2aX3Fd0NTHadzTILKufFCbeGrBnhZaCow6DOLBs9VSfhmrV1lyP8cWPZyVeyLn3g"
        self.executive_producer_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzE5OWEzNDAyODUwMDcxNjAzMjdlIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE0MDcxNTksImV4cCI6MTYxMTQ5MzU1OSwiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.tlkgAF1sHoffJW3YDdLFf3C0iBPbVepBa3J3gJ3I2ZzK5xjAUj6QrAFwf8XXI6PwZ7bNbPjjBJ4ANg9ugCeupkTPO7_N7q0sKVTFaS_qCTh04nq8EFQ01BcGCcxUw1lFP9uTDdDWNSKDyJFwI-oDoZgsbigxNNIQF80clnlXrWVP5c6aVf7ntLMr6mNadCerv8MnC6oLmIp08zaKnQNvJ4xAeo3U6SjopKI-txjYd33NGI1LlFo8z31JXkj5Yhof4FQSszQb7nAaHft77PyAS4mWN293ie9F17r9HRVIC61U5NulZRAw-iWj9t72oa8TqCvOQLdSiXu5vzYnzIYj_w"
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