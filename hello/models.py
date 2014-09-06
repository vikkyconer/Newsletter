from mongoengine import *
from testing.settings import DBNAME
connect(DBNAME)
# Create your models here.

class Authn(Document):
    fname = StringField(required=True)
    lname = StringField(required=True)
    uname = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    lastlogin = DateTimeField(required=True)
