from google.appengine.ext import ndb

class ImageItem(ndb.Model):
    data = ndb.BlobProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

def put(data):
    item = ImageItem(data=data)
    return item.put().urlsafe()

def get(key):
    item = ndb.Key(urlsafe=key).get()
    if not item:
        return None
    return item.data, item.date
