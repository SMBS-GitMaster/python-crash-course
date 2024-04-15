"""
A basic User class. This SQLAlchemy model will be used to create a table in the database.

The table will have the following columns:
- id: A unique identifier for each user.
- public_id: A public unique identifier for each user. We use a public_id because we don't want to expose the id of the user in the API.
- name: The name of the user.
- email: The email of the user.
- password: The password of the user. This will be hashed before storing it in the database.
"""
import jwt
from db import db
from flask import current_app as app
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def serialize(self):
        return {
            'public_id': self.public_id,
            'name': self.name,
            'email': self.email
        }

    def encode_auth_token(self):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': self.public_id
        }

        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY')
        )

    @staticmethod
    def decode_auth_token(auth_token):
        return jwt.decode(auth_token, app.config.get('SECRET_KEY'), algorithms=['HS256'])

