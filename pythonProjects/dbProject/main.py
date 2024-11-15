from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api()

courses = {1:{"name": "python","videos":21}, 2:{"name": "java", "videos":2}}

class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        return courses[course_id]

    def delete(self, course_id):
        del courses[course_id]
        return courses

api.add_resource(Main, '/api/main/courses/<int:course_id>')
api.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
