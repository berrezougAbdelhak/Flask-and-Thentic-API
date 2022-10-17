from db import db 

class UserModel(db.Model):
    __tablename__="users"
    
    id_user=db.Column(db.Integer,primary_key=True)
    address_account=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self,address,password) -> None:
        self.address_account=address
        self.password=password

    @classmethod
    def find_by_address(cls,address):
        return cls.query.filter_by(address_account=address).first()
    
    def json(self):
        return {"address" : self.address_account}


    


        