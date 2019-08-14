import webapp2
import jinja2
import os
from app_models import Major, ANCESTORY_KEY
from data_init import seed_data

jinja_env =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 

def GetMajors():
    majors = []
    
    for i in Major.query(ancestor=ANCESTORY_KEY).order(Major.name).fetch():
        majors.append(i.name)
    
    majors.append("Other")
    return majors

class MainPage(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('/templates/index.html')
        seed_data()
        vals = {"majors":GetMajors()}
        self.response.write(t.render(vals))

    def post(self):
        t = jinja_env.get_template('/templates/index.html')
        vals = {"majors":GetMajors()}
        self.response.write(t.render(vals))

routes = [('/',MainPage)]
app = webapp2.WSGIApplication(routes, debug=True)

