from mongoengine import connect
from models import *

connect("rent_items", host="localhost", port=27017)

def add_user(user_name, user_surname):
    user = User.objects(user_name=user_name, user_surname=user_surname).first()

    if not user:
        user = User(user_name=user_name, user_surname=user_surname)
        user.save()
        return user

    return False

def remove_user(user_id):
    user = User.objects(id=user_id).first()

    if user:

        Rent.objects(user=user).delete()
        print(f"Користувач {user.user_name} {user.user_surname} видалений")
        user.delete()
        return True

    print(f"Нема {user_id}")
    return False

def get_user_by_id(user_id):
    user = User.objects(id=user_id).first()
    if user:
        return {'id':str(user.id), 'user_name': user.user_name, 'user_surname': user.user_surname}
    return None


def get_users_json():
    users = User.objects.all()
    if users:
        return [{'id':str(user.id), 'user_name': user.user_name, 'user_surname': user.user_surname} for user in users]

    return []
###############################################################################################################

def add_thing(thing_name, count):
    thing = Thing.objects(thing_name=thing_name).first()
    if thing:
        thing.count_things += count
        thing.save()
    else:
        thing = Thing(thing_name=thing_name, count_things=count)
        thing.save()
        return thing


def delete_thing_by_name(thing_id):
    thing = Thing.objects(id=thing_id).first()

    if thing:
        Rent.objects(thing=thing).delete()
        print(f"Предмет {thing.thing_name} видалений")
        thing.delete()
        return True

    print(f"Нема {thing_id}")
    return False


def get_things_json():
    things = Thing.objects.all()
    if things:
        return [{'id': str(thing.id),'thing_name': thing.thing_name, 'count': thing.count_things} for thing in things]
    return []
##############################################################################################################

def find_id_thing_by_name(thing_name):
    thing = Thing.objects(thing_name=thing_name).first()
    if thing:
        return thing.id
    return None

def find_id_user_by_name_surname(user_name, user_surname):
    user = User.objects(user_name=user_name, user_surname=user_surname).first()
    if user:
        return user.id
    return None

############################################################################################################

def add_rent(user_id, thing_id, count):
    if user_id and thing_id:
        thing = Thing.objects(id=thing_id).first()

        if thing.count_things >= count:
            thing.count_things -= count
            thing.save()

            rent = Rent.objec   ts(user=User.objects(id=user_id).first(), thing=Thing.objects(id=thing_id).first()).first()
            if rent:
                rent.count += count
                rent.save()
                return rent
            else:
                rent = Rent(user=User.objects(id=user_id).first(), thing=Thing.objects(id=thing_id).first(), count=count)
                rent.save()
                return rent

    return print("Нема користувача або предмету")


def give_back_rent(rent_id):
    rent = Rent.objects(id=rent_id).first()
    if rent:
        thing = Thing.objects(id=rent.thing.id).first()
        thing.count_things += rent.count
        thing.save()
        rent.delete()

        return True
    else:
        print("Нема бронювання")
        return False


def update_rent(rent_id, count):
    rent = Rent.objects(id=rent_id).first()
    if rent:
        thing = Thing.objects(id=rent.thing.id).first()
        if rent:
            if rent.count > count:
                thing_count = count - rent.count
                thing.count_things -= thing_count
            elif rent.count < count:
                thing_count = rent.count - count
                thing.count_things += thing_count

            rent.count = count
            thing.save()
            rent.save()
        return rent


def get_rents_json():
    rents = Rent.objects.all()

    if rents:
        return [{'id': str(rent.id),
                 'user_id': str(rent.user.id) if rent.user else None,
            'thing_id': str(rent.thing.id) if rent.thing else None,
                 'count': rent.count} for rent in rents]
    return []