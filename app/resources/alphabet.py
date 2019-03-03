from flask_restful import Resource, reqparse
from flask.views import MethodView
from ..models import AlphabetSchema, Alphabet   

class AlphabetAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('image_path',
        type=str,
        required=True,
        help="The description image of word in question"
    )
    parser.add_argument('file_name', type=str, help='The name of the video')
    
      
    def get(self):
        words_schema = AlphabetSchema(many=True)
        results = words_schema.dump(Alphabet.get_all()).data      
        return results    
        
    def post(self):
        data = AlphabetAPI.parser.parse_args()
        print(data)
      
        try:
            course_name = data['name']
            file_name = data['file_name']
            image_path = data['image_path']

            # Save course in db with filename as the key for accessing the file from S3  
            new_course = Alphabet(name=course_name, file_name=file_name)             
            new_course.save()            
            #Upload file to S3             
            s3.upload_file(image_path, bucket_name, file_name)
            return {'message': "Alphabet Word Added Succesfully"}, 200
        except:
            return {'message': " An error occured inserting the item."}, 500

        return member.json(), 201

    def delete(self):
            
        return {'message':'Item deleted'}

    def put(self, name):
        
        item.save_to_db()

        return item.json()
