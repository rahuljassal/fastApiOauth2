from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
form datetime import datetime, timedelta

SECRET_KEY = "790b73f9e01c815ba879be2b6407fccd79388ec48c6620a2e30018ad8cb64736"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_db = {
    "tim": {
        "username": "tim",
        "full name": "Tim Ruscica",
        "email": "tim@gmail.com",
        "hashed password": "",
        "disabled": False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class User (BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    disabled: bool or None = None


class UserInDB(User):
    hashed_password: str


app = FastAPI()


class Data(BaseModel):
    name: str


@app.post("/create")
async def create(data: Data):
    return {"data": data}


@app.get("/test/{item_id}")
async def test(item_id: str, query: int):
    return {"data": item_id}
