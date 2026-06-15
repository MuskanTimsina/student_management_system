from jose import jwt
SECRET_KEY="Muskan123"
ALGORITHM="HS256"

def create_access_token(data:dict):
    token= jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token