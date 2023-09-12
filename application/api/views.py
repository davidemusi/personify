from flask import request
from flask_restx import Namespace, Resource, fields
from ..model.persons import Person
from ..utils import db
from http import HTTPStatus

api_namespace = Namespace('routes', description='name space for person routes')


person_model = api_namespace.model(
    'Person', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A name"),
        'age': fields.Integer(required=True, description="An age"),
        'email': fields.String(required=True, description="An email")
    }
)



@api_namespace.route('/')
class CreatePerson(Resource):
    
    
    @api_namespace.expect(person_model)
    @api_namespace.marshal_with(person_model)
    def post(self):
        """
            Ceate a person
        """
        data = request.get_json()
        # data = {"name":"David", "email": "age": 30, "david.gmail.com"}

        new_person = Person(
            name = data.get('name'),
            age = data.get('age'),
            email = data.get('email')
        )
        
        new_person.save()

        return new_person, HTTPStatus.CREATED

@api_namespace.route('/<string:name>')
class GetUpdateDeletePerson(Resource):

    @api_namespace.marshal_with(person_model)
    @api_namespace.doc(
        description='Get a persons by name'
    )
    def get(self, name):
        """
            Get a person by name
        """
        person = Person.query.filter_by(name=name).first()

        return person, HTTPStatus.OK
    
    @api_namespace.expect(person_model)
    @api_namespace.marshal_with(person_model)
    @api_namespace.doc(
        description='Update a person by name',
        params = {
            'name': 'A person name'
        }
    )
    def put(self, name):
        """
            Update a Person by name
        """
        person_to_update = Person.query.filter_by(name=name).first()

        data = api_namespace.payload

        person_to_update.name = data["name"]
        person_to_update.age = data["age"]
        person_to_update.email = data["email"]

        db.session.commit()

        return person_to_update, HTTPStatus.OK
    
    
    @api_namespace.doc(
        description='Delete a person by name',
        params = {
            'person name': 'Name of a person'
        }
    )
    def delete(self, name):
        """
            Delete a person by name
        """

        person_to_delete = Person.query.filter_by(name=name).first()

        person_to_delete.delete()

        return {"message": "Deleted Successfully"}, HTTPStatus.OK



