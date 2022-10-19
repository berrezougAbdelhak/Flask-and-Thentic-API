from flask_restful import Resource,reqparse
from models.users import UserModel


class userRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("address",type=str,required=True,help="You have to add an address of the user")
    parser.add_argument("password",type=str,required=True,help="You have to add a password of the user")


    def get(self,address):
        user=UserModel.find_by_address(address)

        if user:
            return user.json()
        return {"message":"The user with the address {} does not exist".format(address)}
    
    def post(self):
        data=userRegister.parser.parse_args()
        if UserModel.find_by_address(data["address"]):
            return {"message": "The user with the address {} already exists".format(data["address"])}
        user=UserModel(data["address"],data["password"])
        user.save_to_db()

        return {"message" : "User created successfuly "},201




