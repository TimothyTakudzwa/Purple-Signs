from flask_restful import Resource, reqparse
from ..models import User
from werkzeug.security import generate_password_hash

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('surname',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('username',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('email',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('phone',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('password',
        type=str,
        
        help="this field cannot be left blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        print(data)
        if User.find_by_username(data['username']):
            return {'message':'username already exists', }, 400
        else:
            
            user = User(username=data['username'],first_name=data['first_name'],surname=data['username'], phone=data['phone'], email=data['email'], 
                password_hash=generate_password_hash(data['password']))
            user.save()

            return {'message': 'user created succesfully'}, 201