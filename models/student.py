from db import db 

class StudentModel(db.Model):
    __tablename__="students"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.Text())
    password=db.Column(db.Text())

    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
