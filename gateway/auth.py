from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import jwt

SECRET_KEY = "meu-segredo-super-seguro"


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if credentials:
            try:
                payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Token is expired")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="Invalid token")
        else:
            raise HTTPException(status_code=403, detail="Credenciais de autenticação ausentes")