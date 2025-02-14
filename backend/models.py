from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_filename = db.Column(db.String(120), nullable=False)
    job_description_filename = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Float, nullable=False)
    suggestions = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Upload {self.id}>'