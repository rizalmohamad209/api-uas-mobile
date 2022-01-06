from app import db
from sqlalchemy.sql import func


class Berita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())

    def __init__(self, image, title, content):
        self.image = image
        self.title = title
        self.content = content
