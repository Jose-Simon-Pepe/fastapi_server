from pydantic import BaseModel

class User(BaseModel):
    email:str
    password:str
    roles:int 
    id:None | str

