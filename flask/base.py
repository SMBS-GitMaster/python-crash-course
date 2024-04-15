import os
import uuid

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from middleware import requires_authentication
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# We're using sqlite as our database. We'll store the database in the same directory as the app.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, os.getenv('DATABASE_NAME', 'app.db'))
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# Let's initialize the db
from db import db
db.init_app(app)

# We have a model class called TODO, which is a subclass of db.Model. This class will be used to create a table in the database.
from models.Todo import Todo
from models.User import User

# This will create the table in the database.
with app.app_context():
    db.create_all()

"""
We're gonna create 4 endpoints:

/todo: GET - Retrieves all of the TODOs created so far
− /todo/create: POST - Allows you to create a TODO
o Validate that the title is never longer than 255 characters
o Validate that the description is never longer than 65535 characters
− /todo/update/<id>: PUT - Allows you to edit a specific TODO.
o You’ll receive the ID as a query parameter and the details as body.
o The owner cannot be edited once it’s created, so don’t receive it as a
parameter here.
− /todo/delete/<id>: DELETE - Allows you to remove a specific TODO.
"""

@app.route('/todo', methods=['GET'])
@requires_authentication
def get_todos(user):
    todos = (
        Todo.query
        .filter_by(owner = user.public_id)
        .all()
    )

    return jsonify([todo.serialize() for todo in todos])

@app.route('/todo/create', methods=['POST'])
@requires_authentication
def create_todo(user):
    data = request.get_json()
    if len(data['title']) > 255:
        return jsonify({'error': 'Title is too long!'}), 400
    if len(data['description']) > 65535:
        return jsonify({'error': 'Description is too long!'}), 400

    # Create a new Todo object. The owner of the Todo will be the current user.
    todo = Todo(owner=user.public_id, title=data['title'], description=data['description'])

    # Add the Todo to the database and commit the changes.
    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.serialize())

@app.route('/todo/update/<id>', methods=['PUT'])
@requires_authentication
def update_todo(user, id):
    data = request.get_json()
    todo = Todo.query.get(id)

    # Check if the current user owns this Todo
    if user.public_id != todo.owner:
        return jsonify({'error': 'You do not own this Todo!'}), 403

    if len(data['title']) > 255:
        return jsonify({'error': 'Title is too long!'}), 400
    if len(data['description']) > 65535:
        return jsonify({'error': 'Description is too long!'}), 400

    todo.title = data['title']
    todo.description = data['description']

    db.session.commit()

    return jsonify(todo.serialize())

@app.route('/todo/delete/<id>', methods=['DELETE'])
@requires_authentication
def delete_todo(user, id):
    # Check if the current user owns this Todo
    if user.public_id != Todo.query.get(id).owner:
        return jsonify({'error': 'You do not own this Todo!'}), 403

    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()

    return jsonify(todo.serialize())

"""
Additionally, we're gonna create 2 more endpoints to handle user registration and user login
"""
@app.route('/login', methods =['POST'])
def login():
    data = request.form

    if not data or not data.get('email') or not data.get('password'):
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm="Login required"'}
        )

    user = User.query\
        .filter_by(email = data.get('email'))\
        .first()

    if not user:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm="User does not exist"'}
        )

    if check_password_hash(user.password, data.get('password')):
        try:
            token = user.encode_auth_token()
            return make_response(jsonify({'token' : token}), 200)
        except Exception as e:
            print('An error occurred while generating the token.', e)
            return make_response(jsonify({'message' : "Unable to login."}), 201)

    return make_response(
        'The password provided is incorrect',
        403,
        {'WWW-Authenticate' : 'Basic realm="The password provided is incorrect"'}
    )

# signup route
@app.route('/signup', methods =['POST'])
def signup():
    data = request.form

    name, email = data.get('name'), data.get('email')
    password = data.get('password')

    user = User.query\
        .filter_by(email = email)\
        .first()

    if not user:
        user = User(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        return make_response('User already exists. Please Log in.', 202)

# Let's run the app
if __name__ == '__main__':
    app.run(debug=True)
