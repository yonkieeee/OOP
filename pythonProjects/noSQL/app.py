from flask import Flask, request, jsonify
from flask_restful import Api
from db_methods import *
from mongoengine import connect
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api()
connect('rent_items', host="localhost", port=27017)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data['user_name']
    user_surname = data['user_surname']

    if not user_name or not user_surname:
        return {"error": "Не має ім'я або прізвище"}, 400

    try:
        add_user(user_name, user_surname)
        return {"message": "Юзер доданий"}, 201
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": str(e)}, 500


@app.route('/user', methods=['GET'])
def get_users():
     return jsonify(get_users_json())

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(get_user_by_id(user_id))


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not user_id:
        return {"error": "Не має user_id"}, 400

    try:
        remove_user(user_id)
        return {"message": "Юзер видалений"}, 201
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": str(e)}, 500


#########################################################################################################

@app.route("/thing", methods=["POST"])
def create_things():
    data = request.get_json()
    thing_name = data['thing_name']
    thing_count = data['thing_count']

    if not thing_name or not thing_count:
        return {"error": "Не має назви або кількості"}, 400

    if not str(thing_count).isdigit():
        return {"error": "Count має бути числом"}, 400

    try:
        add_thing(thing_name, int(thing_count))
        return {"message": "Предмет доданий"}, 201
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": str(e)}, 500

@app.route("/thing", methods=["GET"])
def get_things():
    return jsonify(get_things_json())


@app.route("/thing/<thing_id>", methods=["DELETE"])
def delete_thing(thing_id):
    if not thing_id:
        return {"error": "Не має назви"}, 400
    try:
        delete_thing_by_name(thing_id)
        return {"message": "Юзер видалений"}, 201
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": str(e)}, 500

###################################################################################################################

@app.route("/rent", methods=["POST"])
def create_rent():
    data = request.get_json()
    user_id = data['user_id']
    thing_id = data['thing_id']
    count = data['count']

    if not user_id or not thing_id or not count:
        return {"error": "Шось Не має"}, 400

    if not str(count).isdigit():
        return {"error": "Count має бути числом"}, 400

    try:
        add_rent(user_id, thing_id, int(count))
        return {"message": "Rent доданий"}, 201
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": str(e)}, 500


@app.route("/rent/<rent_id>/", methods=["DELETE"])
def delete_rent(rent_id):
    if not rent_id:
        return {"error": "Шось Не має"}, 400

    try:
        give_back_rent(rent_id)
        return {"message": "рент видалиний"}, 201
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": str(e)}, 500

@app.route("/rent/<rent_id>", methods=["PATCH"])
def change_rent(rent_id):
    data = request.get_json()
    count = data.get('count')

    if count is None:
        return {"error": "Не вказано кількість для оновлення"}, 400

    try:
        rent = update_rent(rent_id, int(count))

        if rent:
            return {"message": "Оренду оновлено", "rent_id": str(rent.id)}, 200
        else:
            return {"error": "Не знайдено оренди для вказаного користувача або предмета"}, 404
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {"error": "Сталася помилка при оновленні оренди", "details": str(e)}, 500

@app.route("/rent", methods=["GET"])
def get_route():
    return jsonify(get_rents_json())


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')