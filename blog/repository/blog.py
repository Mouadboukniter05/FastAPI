from fastapi import HTTPException,status,Response
from sqlalchemy.orm import Session

from .. import schemas
from .. import models

#---------------------------------------------------------------------------------------#
def allBlog(db:Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no blogs")
    return blogs
#---------------------------------------------------------------------------------------#
def createUser(b:schemas.Blog,db:Session):
    new_blog = models.Blog(title=b.title,body=b.body,user_id=b.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def findByID(id:int,response: Response,db:Session):
    blog =  db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
    return blog
def deleteById(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"

def update(id:int,req:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    
    print(req)
    blog.update({models.Blog.title: req.title,models.Blog.body : req.body}, synchronize_session=False)
    db.commit()
    return "updated"

    