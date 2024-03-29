from pydantic import BaseModel
from typing import List,Union

class BlogBase(BaseModel):
    title:str
    body:str
    user_id:int
    
class Blog(BlogBase):
      class Config():
            orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
    class Config():
            orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] 
    class Config():
            orm_mode = True

class ShowBlog(Blog):
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None