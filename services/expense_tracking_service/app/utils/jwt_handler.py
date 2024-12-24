import os
import jwt
from werkzeug.exceptions import Unauthorized
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def decode_jwt(auth_header):
    """
        Decodes a JWT token to extract user information.
        
        :param auth_header: The Authorization header containing the JWT token.
        :return: Decoded JWT payload.
        :raises Unauthorized: If the token is invalid or missing.
    """
    if not auth_header or not auth_header.startswith("Bearer "):
        raise Unauthorized("Missing or invalid Authorization header.")
    
    token = auth_header[len("Bearer "):]  # Remove 'Bearer ' prefix
    try:
        # Read SECRET_KEY from environment variables (loaded from .env)
        secret_key = os.getenv("SECRET_KEY")
        if not secret_key:
            raise Unauthorized("SECRET_KEY not found in environment variables.")
            
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Unauthorized("Token has expired.")
    except jwt.InvalidTokenError:
        raise Unauthorized("Invalid token.")
