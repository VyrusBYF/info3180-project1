# pylint: disable=E1101

from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    gender = db.Column(db.String(30))
    bio = db.Column(db.String(300))
    file = db.Column(db.String(300))
    join_date = db.Column(db.String(80))

    def __init__(self, firstname, lastname, email, location, gender, bio, file, join_date):
        self.firstname  = firstname 
        self.lastname = lastname
        self.email = email
        self.location = location
        self.gender = gender
        self.bio = bio
        self.file = file
        self.join_date = join_date

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.firstname)
