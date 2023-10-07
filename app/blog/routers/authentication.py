from fastapi import APIRouter, HTTPException,status,Depends
from fastapi.security import  OAuth2PasswordRequestForm
from blog.JWTtoken import create_access_token
from blog import schemas,models,database
from typing import List
from sqlalchemy.orm import Session 
from blog.hashing import Hash
from blog.repository import user


router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(req :  OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials')
    if not Hash.verify_password(req.password,user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect password')
    #generate a jwt token and return
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}