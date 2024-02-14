from . import db

class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    mbti = db.Column(db.String(4), nullable=False)
    collabo_style = db.Column(db.String(100), nullable=False)
    advantage = db.Column(db.String(200), nullable=False)
    blog_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<TeamMember {self.username}>'
