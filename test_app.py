import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Actors, Movies
from app import create_app


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.db_path = os.environ['DATABASE_URL']
        self.token = os.environ['TOKEN_TEST']
        setup_db(self.app, self.db_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = {
            "name": "lithika",
            "age": 10,
            "gender": "female"
        }

        self.new_movie = {
            "title": "Frozen II",
            "releasedate": "12-06-2019"
        }

        self.update_actor = {
            "name": "Sam"
        }

        self.update_movie = {
            "title": "Cars"
        }

        # Valid Token passed from environment
        self.authorization = {
            "Authorization": self.token
        }

        # Invalid Token
        self.authorization_exp = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ4MnRCdnd5T2ZNRUdnRVlwX3VoRSJ9.eyJpc3MiOiJodHRwczovL3NoYWxpbmktZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiNUt2Wm45eXhwUEE4WHZWZ1k0MFNFejNBMzJ2N0xWaW1AY2xpZW50cyIsImF1ZCI6IkNhcHN0b25lQVBJIiwiaWF0IjoxNTkwMjUyNjkzLCJleHAiOjE1OTA4NTc0OTMsImF6cCI6IjVLdlpuOXl4cFBBOFh2VmdZNDBTRXozQTMydjdMVmltIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOltdfQ.VpsZK_eKlqgjlMS1UNZALh6TX69eUrGRIMAgUi0HSO6s1NIBoHQdEIuuttZt39lGPCY8yf5H_ODlWaLmYSdOfj2y0xEmD80TyaY_cbu1LQtbb9vVsoZlyFU6E-CLH38btQybTyjYngcVRz_LEfxD-ZUVAT6k78cyFlVqGbIrilR-FMKQ6U3NC6VOXdA9c0uPjLfd8e2qqjl6Zq3YnYCYjP4TI-9Q98xYJiI360PEStGSdYS2ksbCLSwxqRDPjXtcIygnNUQvOS3uI-sJwb66l7dl5uxPdAFto_WClhL9f65Ip2ZZkip6cmSPOcvuTeiJeDUGQpTRWjeLT_MQqbv3gw"
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_1_get_api_request(self):

        res = self.client.get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['Message']))

    def test_2_create_actors(self):

        res = self.client.post('/actors', json=self.new_actor, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_3_create_movies(self):

        res = self.client.post('/movies', json=self.new_movie, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_4_get_actors(self):

        res = self.client.get('/actors', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_5_get_movies(self):

        res = self.client.get('/movies', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_6_get_actors_by_id(self):

        res = self.client.get('/actors/1', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_7_get_movies_by_id(self):

        res = self.client.get('/movies/1', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_8_update_actors(self):

        res = self.client.patch('/actors/1', json=self.update_actor, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_9_update_movies(self):

        res = self.client.patch('/movies/1', json=self.update_movie, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_x_404_get_actors_by_id(self):

        res = self.client.get('/actors/100', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_x_404_get_movies_by_id(self):

        res = self.client.get('/movies/100', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_x_404_delete_actors_not_exist(self):

        res = self.client.delete('/actors/;;;', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_x_404_delete_movies_not_exist(self):

        res = self.client.delete('/movies/;;;', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_x_404_update_actors(self):

        res = self.client.patch('/actors/100', json=self.update_actor, headers=self.authorization,)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_x_404_update_movies(self):

        res = self.client.patch('/movies/100', json=self.update_movie, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_x_delete_actors(self):

        res = self.client.delete('/actors/1', headers=self.authorization, )
        data = json.loads(res.data)

        actors = Actors.query.filter(Actors.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actors, None)

    def test_x_delete_movies(self):

        res = self.client.delete('/movies/1', headers=self.authorization, )
        data = json.loads(res.data)

        movies = Movies.query.filter(Movies.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movies, None)

    def test_x_401_auth_missing(self):

        res = self.client.get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_x_403_unauthorized(self):

        res = self.client.get('/actors', headers=self.authorization_exp, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')


if __name__ == "__main__":
    unittest.main()
