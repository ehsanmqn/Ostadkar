import datetime

from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

class OtherInput(EmbeddedDocument):
    key = fields.StringField(required=True)
    value = fields.DynamicField(required=True)

class Feed(Document):
    sender = fields.StringField(default="", required=True)
    datetime = fields.DateTimeField(default=datetime.datetime.now(), required=True)
    priority = fields.DecimalField(default=0, required=True)
    description = fields.StringField(default="", required=True)
    others = fields.ListField(fields.EmbeddedDocumentField(OtherInput))
