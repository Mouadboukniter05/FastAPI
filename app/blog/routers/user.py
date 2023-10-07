from fastapi import APIRouter,status,Depends
from blog import schemas
from typing import List
from sqlalchemy.orm import Session 
from blog.database import get_db
from blog.repository import user


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

#------------------------------------------------USERS-------------------------------------------------------#



@router.get("/{id}",status_code=200,response_model=schemas.ShowUser)
def getUserById(id:int,db:Session = Depends(get_db)):
    return user.getUserByID(id,db)
#--------------------------------------------------------------------------------------#

@router.post("",status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request : schemas.User,db:Session = Depends(get_db)):
    return user.create_user(request,db)
#---------------------------------------------------*-#
@router.get('',response_model=List[schemas.ShowUser])
def allUsers(db:Session = Depends(get_db)):
    return user.allUsers(db)