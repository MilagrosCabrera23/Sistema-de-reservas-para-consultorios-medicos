from datetime import datetime, timezone, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

ALGORITHM = "HS256"
pdw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pdw_context.hash(password)

def verify_password(plain_password: str, hashed_password:str) -> bool:
    return pdw_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token:str):
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=[ALGORITHM])
    except:
        raise JWTError
    return payload


