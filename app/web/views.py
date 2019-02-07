
from . import web

@web.route('/register', methods=('GET', 'POST'))
def register():
    return '<h1> Hello </h1>'