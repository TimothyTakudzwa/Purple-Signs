from .. import api
from ..models import *
from ..resources.courses import CourseAPI
from ..resources.alphabet import AlphabetAPI
from ..resources.classes import ClassAPI
from ..resources.phrases import PhraseAPI


api.add_resource(CourseAPI, '/api/courses')
api.add_resource(AlphabetAPI, '/api/alphabet')
api.add_resource(ClassAPI, '/api/classes')
api.add_resource(PhraseAPI, '/api/phrase/<int:id>')
api.add_resource(AllSections, '/api/all_sections/<int:id>')
