from app_models import Major, ANCESTORY_KEY
from google.appengine.ext import ndb

#ANCESTORY_KEY = ndb.Key("Major","Major_root")

def seed_data():
    Major(parent=ANCESTORY_KEY,name="English").put()
    Major(parent=ANCESTORY_KEY,name="Mathematics").put()
    Major(parent=ANCESTORY_KEY,name="History").put()
    Major(parent=ANCESTORY_KEY,name="Liberal Arts").put()
    Major(parent=ANCESTORY_KEY,name="Computer Science").put()


