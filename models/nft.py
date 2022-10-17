from ctypes import addressof
from db import db 

class NftModel(db.Model):
    __tablename__="nft"
    
    id_nft=db.Column(db.Integer,primary_key=True)
    address_nft=db.Column(db.String(80))


    def __init__(self,address) -> None:
        self.address=address

