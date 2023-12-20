from entities.user import User
class SignUp:
    def create_user(self,user:User=None,db:list=None):
        if not "@" in user.email:
            raise ValueError()
        for former_user in db.get_all():
            if former_user.email == user.email:
                raise ValueError()
        db.save(user=user)
