"""
A basic User class. This SQLAlchemy model will be used to create a table in the database.

The table will have the following columns:
- id: A unique identifier for each user.
- public_id: A public unique identifier for each user. We use a public_id because we don't want to expose the id of the user in the API.
- name: The name of the user.
- email: The email of the user.
- password: The password of the user. This will be hashed before storing it in the database.
"""
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

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
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': self.public_id
            }

            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        return jwt.decode(auth_token, app.config.get('SECRET_KEY'))
