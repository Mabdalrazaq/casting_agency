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
        self.casting_assistant_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzNkM2QzNDAyODUwMDcxNjAzNDIxIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE3NTk1MjQsImV4cCI6MTYxMTg0NTkyNCwiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.SZrowdJAlDRZwNyOpDyIvnD74g4HrHJim60hj4A1IqaHw4didkBAZGxi3TCsM2v_6lK0dlSR1tv2gwkhx_O_AR65kt9dtnZyISa-6Qh_I0zuZobsP3B27u_mVd9BmuSTxJlZEgfgylHVIUQFwK74eUya9jV_6KL2SN0JzJ2pQ1jqx_MhEeJBiCYDdDlLaeQRg-46d-l1EIHqjVB4Prw-bdDzrUEJZuoNG8TxFE2pXo4NzfL_E8KigxQDd3ZpgYyEwG2x12MC-eKobgbdp0qkExOPE7oRT0nvksexPsQPqRJKCEHbyH-Uv5U38a-9TfDCZIqaM9VFXmXcneDKExYmkg"
        self.casting_director_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzNjYmVmZmNiZTIwMDZhODg1ZmRiIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE3NTkzNzMsImV4cCI6MTYxMTg0NTc3MywiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.w0vuLmHVYeklBNMk4O1ZQHTO9V8sdnBr3_Rvh_HqJ1fNeJt6yh_svdSJ5CtpkQ8l5iWgJp5HR7SdLeatHtUjPDgm-mMBLjplbEE3lM3zLZLwrSUB597FsEf6KjUj1ZwU__YArTbeFxW5RUbYQCJGGkf_ZL-r-DuovAXC_V2HAWtg4T4z9iiPdtbGWYDPgE2XOdINTxTI6OZf7zpOoYVitf5gjon0B2ZyLLnOjTYPLYehunu65DI9jAgBRTBPA5fKYhSj8x5OpkneGNjuxnHJpLKudmGOSNUa8tNVP-pReEUwmmrGt3tjmdUMA2mRurEFBP2Mxm2iUfpzRYfRNrLc-w"
        self.executive_producer_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzE5OWEzNDAyODUwMDcxNjAzMjdlIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE3NTkyNTcsImV4cCI6MTYxMTg0NTY1NywiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Nj---xU9kHTffIZF4IUG1FGbdE4nmPAXDnQDSETBkFwUjE00rSH2NrWTCdktyF02705b8Sr8R3vn3nKHdfTpI6yrw1MLg-9FILwK2ogbzaE-30vpfFmrUpaB0I2KmgmVTOvOaJL_5g2V9yoxwitaiFD__4Mk5Hmb_sEwo1IIYRe-q1ueN_9MC_zm5ouTLCsMlMUSWLJIvmq0tyUnGkl-UkFao6fQ1n-oHJ9PTXUwRBLJvkQjgkoq7LfgOkQXxYW_a2MOYoHUZ6pdTfRj8vFw8BQvn6DO46Nud_8Ov9cYsuvAuFYZ9M50hjj5YSRF_eZH9KqwOyplMxaP2JpCkMr9vQ"
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