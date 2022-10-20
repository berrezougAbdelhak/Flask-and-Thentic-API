from flask import Flask
from flask_restful import Api
from ressources.userResource import userRegister
from flask_jwt import JWT
from models import users
from models import nft
from ressources.studentResource import studentRegister 
from security import authenticate,identity
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
# app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:08087898@localhost:5432/thenticDB"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key="Azerty"

api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)

api.add_resource(userRegister,"/register") 
# api.add_resource(studentRegister,"/register") 
if __name__=="__main__":
    from db import db 
    db.init_app(app)
    app.run(port=5000,debug=True)
