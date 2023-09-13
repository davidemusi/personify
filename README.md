# Personify API
Personify API is a simple RESTful web service built using Flask and Flask-RESTx. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a collection of persons.
## Features
- Create a new person with a name, age, and email.
- Retrieve a person by name.
- Update a person's information by name.
- Delete a person by name.
## Getting Started
These instructions will help you set up and run the Personify API on your local machine for development and testing purposes.
### Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.11 installed.
- [Pipenv](https://pipenv.pypa.io/en/latest/) installed (for managing dependencies).
- SQLite or another compatible database.
### Installation
1. Clone the repository:
   ~~~ bash
   git clone https://github.com/yourusername/Personify.git
   cd Personify
   ~~~
2. Create a virtual environment and install dependencies:
   ~~~ bash
   pipenv install

   pipenv shell
   ~~~
3. Initialize the database:
   ~~~ bash
   flask db init
   flask db migrate
   flask db upgrade
   ~~~

## Usage

1. Start the development server:
   ~~~ bash
   flask run
   ~~~
2. The API is now running locally. You can access it at:
   ~~~ bash
   http://localhost:5000/api/
   ~~~
3. Use a tool like Postman or curl to interact with the API endpoints.

## API Endpoints
- POST /api/: Create a new person.
- GET /api/<name>: Retrieve a person by name.
- PUT /api/<name>: Update a person's information by name.
- DELETE /api/<name>: Delete a person by name.

For detailed usage instructions and examples, please refer to the API documentation.

## API Documentation

API documentation is generated using Swagger UI and can be accessed at:
   ~~~ bash
   http://localhost:5000/api/doc/
   ~~~

## Testing

   ~~~ bash
   pytest
   ~~~

## Deployment

You can deploy this API to various cloud platforms or your own server. Be sure to set the appropriate environment variables for production.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask and Flask-RESTx for creating the API.
- SQLAlchemy for database management.
