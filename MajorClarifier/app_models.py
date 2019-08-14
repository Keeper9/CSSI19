from google.appengine.ext import ndb

class Major(ndb.Model):
    name = ndb.StringProperty(required=True)

ANCESTORY_KEY = ndb.Key("Major","Major_root")

