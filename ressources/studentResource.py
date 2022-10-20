from flask_restful import Resource,reqparse
from models.student import StudentModel
class studentRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True,help="You have to add a username")
    parser.add_argument("password",type=str,required=True,help="You have to add a password")

    def post(self):
        data=studentRegister.parser.parse_args()
        if StudentModel.find_by_username(data["username"]):
            return {"message" : "User with the username {} already exists ".format(data["username"])}
        student=StudentModel(data["username"],data["password"])
        student.save_to_db()

        return {"message":"User created successfuly"},201
    



