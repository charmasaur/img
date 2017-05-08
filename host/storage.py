from google.appengine.ext import ndb

class ImageItem(ndb.Model):
    # TODO: Maybe we should just store the binary blob..
    bdata = ndb.StringProperty(indexed=False)
    ext = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

def put(bdata, ext):
    item = ImageItem(bdata=bdata, ext=ext, cw_data=cw_data)
    return item.put().urlsafe()

def get(key):
    item = ndb.Key(urlsafe=key).get()
    if not item:
        return None
    return item.bdata, item.ext, item.date
