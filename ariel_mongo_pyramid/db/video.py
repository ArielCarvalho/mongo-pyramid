from pyramid_mongoengine import MongoEngine

from operator import itemgetter


db = MongoEngine()


class Video(db.Document):
    """Simple user model"""
    name = db.StringField()
    theme = db.StringField()
    thumbs_up = db.IntField(default=0)
    thumbs_down = db.IntField(default=0)
