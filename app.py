from flask import Flask
from flask_restful import Api
from ressources.userResource import clientResource
from models import users
app=Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:08087898@localhost:5432/thenticDB"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key="jose"

api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# api.add_resource(clientResource,"/client")
api.add_resource(clientResource,"/item/<string:name>") 
if __name__=="__main__":
    from db import db 
    db.init_app(app)
    app.run(port=5000,debug=True)
