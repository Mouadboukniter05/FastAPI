from fastapi import APIRouter,status,Depends,Response

from blog.oauth2 import get_current_user
from blog import schemas
from typing import List
from sqlalchemy.orm import Session 
from blog.database import get_db
from blog.repository import blog 

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

#-----------------------------------ADD-----------------------------#
@router.post("",status_code=status.HTTP_201_CREATED)
def create(b : schemas.Blog,db:Session = Depends(get_db),current_user:schemas.User = Depends(get_current_user)):
    return blog.createUser(b,db)
    

#-----------------------------------GET-----------------------------#

@router.get("",response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db),current_user:schemas.User = Depends(get_current_user)):
    return blog.allBlog(db)
#-----------------------------------get-----------------------------#

@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def find(id:int,response: Response,db:Session = Depends(get_db),current_user:schemas.User = Depends(get_current_user)):
    return blog.findByID(id,response,db)
#-----------------------------------delete-----------------------------#

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db),current_user:schemas.User = Depends(get_current_user)):
    return blog.deleteById(id,db)
    

#-----------------------------------Update-----------------------------#

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,req:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.User = Depends(get_current_user)):
   return blog.update(id,req,db)