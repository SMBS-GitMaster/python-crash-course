"""
A basic TODO class. This SQLAlchemy model will be used to create a table in the database.

The table will have the following columns:
- id: A unique identifier for each TODO item.
- owner: The owner of the TODO item.
- title: The title of the TODO item.
- description: A description of the TODO item.
"""
from db import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    title = db.Column(db.String(255))
    description = db.Column(db.String(65535))

    def serialize(self):
        return {
            'id': self.id,
            'owner': self.owner,
            'title': self.title,
            'description': self.description
        }
