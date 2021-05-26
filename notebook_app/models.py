
from notebook_app import db, login_manager
from flask_login import UserMixin

from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# ============================== USER MODEL =============================

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.Integer, nullable=False)
	registered_date = db.Column(db.DateTime, default=datetime.utcnow)

	# --- Relationship with Notes Model
	notes = db.relationship('Notes', backref="author", lazy=True)
	subjects = db.relationship('Subjects', backref="subject_author", lazy=True)

	def __repr__(self):
		return f"{self.username}"

# ============================== NOTES MODEL =============================

class Subjects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subjects_name = db.Column(db.String(100), nullable=False)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Subjects('{ self.subjects_name }' )"

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjects = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=False)
    date_saved = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Notes('{self.id}', '{self.date_saved}', '{self.subjects}'), '{self.user_id}')"

# ============================== FEEDBACK MODEL =============================

class Feedbacks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    date_submited = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Feedbacks('{self.name}'"



