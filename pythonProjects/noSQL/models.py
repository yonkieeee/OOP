from mongoengine import Document, StringField, IntField, ListField, ReferenceField


class User(Document):
    user_name = StringField(required=True)
    user_surname = StringField(required=True)

class Thing(Document):
    thing_name = StringField(required=True)
    count_things = IntField(required=True)

class Rent(Document):
    user = ReferenceField(User)
    thing = ReferenceField(Thing)
    count = IntField(required=True)