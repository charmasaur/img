import uuid
from app.app import db

class Image(db.Model):
    __tablename__ = "images"

    key = db.Column(db.String, default=lambda: uuid.uuid4().hex, primary_key=True)
    data = db.Column(db.LargeBinary)

def put(data):
    item = Image(data=data)
    db.session.add(item)
    db.session.commit()
    return item.key

def get(key):
    item = Image.query.filter_by(key=key).first()
    if not item:
        return None
    return item.data
