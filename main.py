from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#----------------------------------------#
class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]


# app is part operation decorator
# operation : get post put delete
@app.get("/")
def index():
    return {"blog":"blog list"}

@app.get("/blog")
def index(limit,published : bool=True,sort : Optional[str]=None):
    if published:
        return {"data":f'{limit} published blogs from the db'}
    else:
        return {"data":f'{limit}  blogs from the db'}


@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished post"}

@app.get("/blog/{id}")
def blogByid(id:int):
    return [{"data":id}]
@app.get("/blog/{id}/comments")
def comments(id:int):
    return [{"data":id}]



@app.post("/blog")
def create_blog(blog:Blog):
    return {'data':f'a new blog is created with {blog.title}'}


   