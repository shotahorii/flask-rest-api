from flask import Flask
from flask_restful import Resource, Api
from flask_restful.utils import cors
import json

app = Flask(__name__)
api = Api(app)


todos = {"todo1": "Remember the milk"}

class HelloWorld(Resource):

    @cors.crossdomain(origin='*')
    def get(self):
        return {'hello':'world'}

class TodoSimple(Resource):

    @cors.crossdomain(origin='https://shotahorii.github.io')
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    @cors.crossdomain(origin='*')
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class DublinRestaurants(Resource):

    @cors.crossdomain(origin='*')
    def get(self):
        with open('storage/dublin_restaurants.json') as f:
            data = json.load(f)
            return data

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/api/<string:todo_id>')
api.add_resource(DublinRestaurants, '/api/dublinrestaurants')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)