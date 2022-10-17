from db import db 

class userModels(db.Model):
    __tablename__="clients"
    
    id_user=db.Column(db.Integer,primary_key=True)
    address_account=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self,address,password) -> None:
        self.address=address
        self.password=password
    


        