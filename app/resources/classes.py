from flask_restful import Resource, reqparse
from flask.views import MethodView
from ..models import ClassSchema, Classes   

class ClassAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('image_path', type=str, help='Rate to charge for this resource')
    
      
    def get(self):
        class_schema = ClassSchema(many=True)
        results = class_schema.dump(Classes.get_all()).data
        print(results)
        return results        

        
    # def post(self):
    #     data = CourseAPI.parser.parse_args()
    #     print(data)
      
    #     try:
    #         course_name = data['name']
    #         description = data['description']
    #         background_image = data['image_path']

    #         new_course = Course(name=course_name, description=description, background_image=background_image)
    #         new_course.save()
    #         return {'message': "Course Created Succesfully"}, 200
    #     except:
    #         return {'message': " An error occured inserting the item."}, 500

    #     return member.json(), 201

    # def delete(self):
            
    #     return {'message':'Item deleted'}

    # def put(self, name):
        
    #     item.save_to_db()

    #     return item.json()
