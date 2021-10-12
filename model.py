from flask import url_for
from app import db

class Mensajes(db.DynamicDocument):
    url = db.StringField()
    date = db.DateTimeField()
    content = db.StringField()
    renderedContent = db.StringField()
    #podemos especificar también el subdocumento user, pero habría que hacer una class user etc.
    #user = db.EmbeddedDocumentField('user')
