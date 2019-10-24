'''
from mongoengine import Document
from mongoengine.fields import (
    FloatField, StringField,
    ListField, URLField, ObjectIdField
)

class Record(Document):
    meta = {'collection': 'record'}
    ID = ObjectIdField()
    name = StringField()
    reason = StringField()
    problems_summary = ListField(StringField())
    diagnostic = StringField()
    initial_planning = StringField()
    consult_notes = ListField(StringField())
    medical_recomendations = ListField(StringField())
    summary = ListField(StringField())
    family_background = ListField(StringField())
    toxic_habits = ListField(StringField())
'''
