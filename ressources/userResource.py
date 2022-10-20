from flask_restful import Resource,reqparse
from models.users import UserModel 
from flask_jwt import jwt_required

class userRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True,help="You have to add an address of the user")
    parser.add_argument("password",type=str,required=True,help="You have to add a password of the user")

    @jwt_required
    def get(self):
        data=userRegister.parser.parse_args()
        user=UserModel.find_by_address(data["username"])

        if user:
            return user.json()
        return {"message":"The user with the address {} does not exist".format(data["username"])}
    
    def post(self):
        data=userRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "The user with the address {} already exists".format(data["address"])}
        user=UserModel(data["username"],data["password"])
        user.save_to_db()

        return {"message" : "User created successfuly "},201



        