from uuid import uuid4,UUID
from entities.user import RegisteredUser 

class RegisteredUserBuilder:
    def __init__(self):
        self._email = "jose.s.contacto@gmail.com"
        self._password ="Password123"
        self._roles = 3
        self._id = str(uuid4()) 

    def with_email(self,email:str=None):
        self._email = email
        return self 

    def with_password(self,password:str=None):
        self._password =password
        return self

    def with_roles(self,roles:int=None):
        self._roles =roles
        return self

    def with_id(self,id:str=None):
        self._id = id
        return self
    
    def build(self):
        return RegisteredUser(email=self._email,
                    password=self._password,
                    roles=self._roles,
                    id=self._id)
