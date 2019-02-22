from .. import api
from ..models import *
from ..resources.courses import CourseAPI
from ..resources.alphabet import AlphabetAPI

api.add_resource(CourseAPI, '/api/courses')
api.add_resource(AlphabetAPI, '/api/alphabet')
api.add_resource(AllPhrases, '/api/all_phrases')
api.add_resource(AllSections, '/api/all_sections/<int:id>')
