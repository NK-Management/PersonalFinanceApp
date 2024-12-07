from flask_jwt_extended import create_access_token, decode_token, get_jwt_identity, jwt_required

def generate_token(user):
    """
    Generates an access token for a user.
    """
    return create_access_token(identity={"id": user.id, "role": user.role.role_name})

def decode_token_data(token):
    """
    Decodes a JWT token.
    """
    return decode_token(token)

@jwt_required()
def get_current_user():
    """
    Retrieves the current user based on the JWT token.
    """
    return get_jwt_identity()
