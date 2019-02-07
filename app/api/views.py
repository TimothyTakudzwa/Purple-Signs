from .. import api
from ..models import *


api.add_resource(AllCourses, '/api/all_courses')
api.add_resource(AllWords, '/api/all_words')
api.add_resource(AllPhrases, '/api/all_phrases')
api.add_resource(AllSections, '/api/all_sections/<int:id>')
