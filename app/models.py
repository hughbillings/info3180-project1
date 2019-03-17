from app import db



class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    location = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    biography = db.Column(db.String(255))
    photograph = db.Column(db.String(500))
    date_joined = db.Column(db.Date())

    def __init__(self, first_name, last_name, gender, location, biography, photograph, email, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.location = location
        self.biography = biography
        self.email = email
        self.photograph=photograph
        self.date_joined = date_joined
       

    

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.first_name
