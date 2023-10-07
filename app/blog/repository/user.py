from fastapi import HTTPException,status,Response
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog import schemas
from blog import models

def getUserByID(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id==id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} not found')
    return user.first()
def create_user(request : schemas.User,db:Session):
    newUser = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
def allUsers(db:Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no users")
    return users
    