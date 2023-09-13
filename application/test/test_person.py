import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from ..model.persons import Person
import json


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config=config_dict['test'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None

    def test_create_person(self):
        data = {
            "name": "John Doe",
            "age": 30,
            "email": "john@example.com"
        }

        response = self.client.post('/api/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        persons = Person.query.all()

        assert len(persons) == 1
        assert response.json['name'] == "John Doe"

    def test_get_person(self):
        response = self.client.get('/api/John Doe')
        
        self.assertEqual(response.status_code, 200)

    def test_update_person(self):
        person_to_update = Person(
            name = 'John Doe',
            age = 30,
            email = 'john@example.com'
        )

        person_to_update.save()

        data = {
            "name": "John Doe",
            "age": 31,
            "email": "newemail@example.com"
        }

        response = self.client.put('/api/John Doe', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_person(self):
        person_to_update = Person(
            name = 'John Doe',
            age = 30,
            email = 'john@example.com'
        )

        person_to_update.save()

        response = self.client.delete('/api/John Doe')
        self.assertEqual(response.status_code, 200)