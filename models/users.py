from db import db 
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__="users"
    
    id_user=db.Column(db.Integer,primary_key=True)
    address_account=db.Column(db.Text())
    password=db.Column(db.Text())

    def __init__(self,address,password) -> None:
        self.address_account=address
        self.password=generate_password_hash(password)

    @classmethod
    def find_by_address(cls,address):
        return cls.query.filter_by(address_account=address).first()
    
    def json(self):
        return {"address" : self.address_account}

    def verify_password(self,pwd):
        return check_password_hash(self.password,pwd)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    


        