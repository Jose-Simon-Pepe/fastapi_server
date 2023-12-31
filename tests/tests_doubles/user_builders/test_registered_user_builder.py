from tests.helpers.user_builders.registered_user_builder import RegisteredUserBuilder


def test_builder_should_return_a_registered_user():
    """
    Instanciamiento de un objeto RegisteredUser siguiendo el esquema siguiente:
    
    class User(BaseModel):
        email:str
        password:str
        roles:int 
        id:None | str
    """
    sut = RegisteredUserBuilder().with_email("jose.s.contacto@gmail.com").build()
    assert type(sut.email) is str 
    assert type(sut.password) is str and len(sut.password)>0
    assert type(sut.roles) is int
    assert type(sut.id) is str

