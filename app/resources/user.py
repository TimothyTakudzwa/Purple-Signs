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
    
    parser.add_argument('phone',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('password',
        type=str,
        
        help="this field cannot be left blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        print("+++++++++++++++++++ My Data ++++++++++++++++++++",data)
        username = data['username'].lower()
        if User.find_by_username(data['username']):            
            return {'message':'username already exists', 'status':1 }, 201      
        else:            
            user = User(username=username,first_name=data['first_name'],surname=data['surname'], phone=data['phone'], 
                password_hash=generate_password_hash(data['password']), paid=False)
            user.save()
            user = User.find_by_username(username)
            user_id = user.id        
            return {'message': 'user created succesfully', 'id': user_id}, 201 

class LoginRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        
        help="This field cannot be left blank")
    parser.add_argument('password',
        type=str,
        
        help="this field cannot be left blank")
        
    def post(self):
        data = UserRegister.parser.parse_args()      
        username = data['username'].lower()
        user = User.find_by_username(username)
        if user is not None and user.check_password(data['password']):
            return {'status':1, 'paid' : user.paid, 'id' : user.id }, 200
        elif user is None:
            return {'status':0, 'paid' : False, 'id' : 0 }, 200
        else: 
            return {'status':0, 'paid' : False, 'id' : user.id }, 200
        # else:
        #     return {'message':'User has no account' }, 400
    
class CheckPayment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        
        help="This field cannot be left blank")
           
    def post(self):
        data = UserRegister.parser.parse_args()      
        username = data['username'].lower()
        user = User.find_by_username(username)
        if user is not None:
            return {'status':1, 'paid' : user.paid }, 200
        else: 
            return {'status':0, 'paid' : False }, 200