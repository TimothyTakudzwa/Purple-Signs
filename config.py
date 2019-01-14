
import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

UPLOAD_FOLDER = 'purple/videos'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'mkv', 'mp4'])

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '931379807056586',
        'secret': '2bfd8b0dd5d928872bd166438cb7b0ae'
    }
}

BASIC_AUTH_USERNAME = 'purple'
BASIC_AUTH_PASSWORD = 'purple'
