from flask import current_app as app
from models import User
from functools import wraps
from flask import jsonify

def requires_authentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        else:
            return jsonify({'message' : 'Missing authorization header'}), 401

        try:
            # We'll use the decode_auth_token() method to decode the token. This method will return the payload of the token.
            # Once we have the payload, we'll use the public_id to query the database for the user.
            data = User.decode_auth_token(token)
            current_user = (
                User.query
                .filter_by(public_id = data['sub'])
                .first()
            )
        except jwt.ExpiredSignatureError:
            return jsonify({
                'message' : 'Signature expired. Please log in again.'
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'message' : 'The authorization token is invalid. Please log in again.'
            }), 401

        # This returns the current user to the route function
        return  f(current_user, *args, **kwargs)

    return decorated

