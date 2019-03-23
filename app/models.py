from . import db, ma
from flask_login import UserMixin
from flask_restful import Api, Resource
from flask_restful.fields import Boolean
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    """ User model defines the user tabel in the database """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120))
    social_id = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(200))
    dob = db.Column(db.Date)
    paid = db.Column(db.Boolean)
   

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_social_id(social):
        return User.query.filter_by(social_id=social).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @staticmethod
    def get_all():
        return Section.query.all()
    
    @staticmethod
    def update_payment(id, paid):
        user=User.query.filter_by(id=id).first()
        print(user)
        user.paid = paid
        user.save()
        return '' 


class Billing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_billed = db.Column(db.Date)
    user_id = db.Column(db.Integer)
    poll_url = db.Column(db.String(2000))
    status= db.Column(db.String(200))
    amount = db.Column(db.Float)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return Billing.query.filter_by(user_id=id).first()
    
    @staticmethod
    def update_payment(id, poll_url):
        user=Billing.query.filter_by(user_id=id).first()
        user.poll_url = poll_url
        user.save()
        return '' 
    
    @staticmethod
    def get_all():
        return Section.query.all()

class Alphabet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    image_path = db.Column(db.String(200))
    file_name = db.Column(db.String(200), unique=True, index=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_by_name(self, name):
        return Alphabet.query.all()

    @staticmethod
    def get_all():
        return Alphabet.query.all()

    def __repr__(self):
        return "<Alphabet: {} {} >".format(self.name, self.file_name)

class Phrases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(200))
    image_path = db.Column(db.String(200))
    class_id = db.Column(db.Integer)
    file_name = db.Column(db.String(200), unique=True, index=True)
     
    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_by_id(id):
       return Phrases.query.filter_by(class_id=id).all()

    @staticmethod
    def get_all():
        return Phrases.query.all()

    def __repr__(self):
        return "<Alphabet: {} {} >".format(self.name, self.file_name)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))  
    description = db.Column(db.String(200))
    background_image = db.Column(db.String(200))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_by_name(self, name):
        return Course.query.all()

    @staticmethod
    def get_all():
        return Course.query.all()


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(200))
    course_id = db.Column(db.Integer)
    file_name = db.Column(db.String(200), unique=True, index=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_course(id):
        return Section.query.filter_by(course_id=id).all()

    @staticmethod
    def get_all():
        return Section.query.all()
   
class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    background_image = db.Column(db.String(200))
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_course(id):
            return Classes.query.filter_by(id=id).all()

    @staticmethod
    def get_all():
        return Classes.query.all()

class CourseSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'background_image')
        model = Course

class ClassSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'background_image')
        model = Classes

class PhraseSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'phrase', 'file_name')
        model = Phrases

class AlphabetSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'file_name')
        model = Alphabet

class SectionSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'section_name', 'course_id', 'file_name')
        model = Section

class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'poll_url', 'user_id')
        model = User

class BillingSchema(ma.ModelSchema):
    class meta:
        fields = ('id', 'poll_url')
        model = Billing  

class AllPhrases(Resource):
    
    def get(self):
        phrase_schema = PhraseSchema(many=True)
        results = phrase_schema.dump(Phrases.get_all()).data       
        return results

class AllSections(Resource):
    
    def get(self, id):
        section_schema = SectionSchema(many=True)
        results = section_schema.dump(Section.find_by_course(id)).data       
        return results  

