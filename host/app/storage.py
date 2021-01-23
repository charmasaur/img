from google.appengine.ext import ndb
from google.net.proto.ProtocolBuffer import ProtocolBufferDecodeError

class ImageItem(ndb.Model):
    data = ndb.BlobProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

def put(data):
    item = ImageItem(data=data)
    return item.put().urlsafe()

def get(key):
    try:
        item = ndb.Key(urlsafe=key).get()
    except TypeError:
        return None
    except ProtocolBufferDecodeError:
        return None
    if not item:
        return None
    return item.data, item.date
