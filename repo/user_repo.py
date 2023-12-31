from servicios.protocols.entityrepo import ENTITY_REPO

class Repo(ENTITY_REPO):
    def __init__(self,db=[]):
        self._db = db

    # OVERRIDE save
    def save(self,user=None,db=None):
        if db is None:
            db = self._db
        if user is not None:
            db.append(user)

    # OVERRIDE save
    def exists(self,user_email:str,db=None) -> bool:
        if db is None:
            db = self._db
        for user in db:
            if user_email == user.email:
                return True
        return False

    # OVERRIDE save
    def get_all(self,db=None) -> list:
        if db is None:
            db = self._db
        return db

    def get_id_by_email(self,email:str=None) -> str:
        if not email ==  None and self.exists(email):
            for user in self._db:
                if user.email == email:
                    return user.id 


    def get_user_by_id(self,id:int):
        for user in self._db:
            if user.id == id:
                return user
