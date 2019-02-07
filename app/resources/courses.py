from flask_restful import Resource, reqparse

class Course(Resource)
    parser = reqparse.RequestParser()

    
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('description',
        type=str,
        required=True,
        help="Every member needs an empcode"
    )

    parser.add_argument(path,
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

   
