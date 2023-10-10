from fastapi import FastAPI
from typing import Annotated

from pydantic import BaseModel
from thiru import add
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import time
app = FastAPI()
SECRET_KEY = "09d25e094faa****************f7099f6f0f4caa6cf63b88e8d3e7dcdcbdcwjedherufhegjfhf!@$%&%^((P))"
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login",scheme_name="JWT")

# def validate_token(token=Depends(OAuth2PasswordBearer(tokenUrl="login",scheme_name="JWT"))):
#     print("token", token)
#     user=token_decode(token)
#     print("user", user)
#     return user

fake_db={"username": "naidu","password": "pual"}
@app.post("/login")
def get_token_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
   
    data={"username":form_data.username, "password":form_data.password}
    print(data)
    if data:
         return {
            "access_token": token_jeneration(data),
            "refresh_token": token_jeneration(data)
        }

    else:
        return "pls provide a valid username and password"


def token_jeneration(data):
    encoded_data = jwt.encode(payload=data,key=SECRET_KEY,algorithm="HS256")
    return encoded_data

def token_decode(token):
    decoded =jwt.decode(token,key=SECRET_KEY,algorithms=['HS256'])

    return decoded
@app.get("/amo")
def read_root(token=Depends(OAuth2PasswordBearer(tokenUrl="login",scheme_name="JWT"))):
    user=token_decode(token)
    if user["username"]==fake_db["username"] and user["password"]==fake_db["password"]:
    
        return {"message": "Hello, World!"}
    else:
        return {"message": "your not in the database"}
@app.get("/add")
async def add_numbers(x: int, y: int , token=Depends(OAuth2PasswordBearer(tokenUrl="login",scheme_name="JWT"))):
    user=token_decode(token)
    if user["username"]==fake_db["username"] and user["password"]==fake_db["password"]:
        
            
        result = add.delay(x, y)
            
        return {"task_id": result.id}
    else:
        return {"message": "your not in the database"}
        


