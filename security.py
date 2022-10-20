from werkzeug.security import safe_str_cmp
from models.users import UserModel
from models.student import StudentModel

# def authenticate(username,password):
#     student=StudentModel.find_by_username(username)
#     if student and safe_str_cmp(student.password,password) :
#         return student

# def identity(payload):
#     student_id=payload["identity"]
#     return StudentModel.find_by_id(student_id)

    
def authenticate(username,password):
    user=UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password) :
        return user
def identity(payload):
    user_id=payload["identity"]
    return UserModel.find_by_id(user_id)


