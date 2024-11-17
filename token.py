import jwt
import datetime

SECRET_KEY = "meu-segredo-super-seguro"

def generate_jwt(payload: dict):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    token = jwt.encode({
        **payload,
        "exp": expiration
    }, SECRET_KEY, algorithm="HS256")

    return token

user_payload = {
    "user_id": 123,
    "username": "joao.silva",
}

token = generate_jwt(user_payload)

print(f"JWT: {token}")
