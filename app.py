from flask import Flask
from flask_restplus import Api, Resource, reqparse

from database import get_city, get_cities, delete_city, add_city, update_city

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


class City(Resource):
    @staticmethod
    def get(city_id):
        city = get_city(city_id)
        return {'id': city.city_id, 'name': city.city_name}

    @staticmethod
    def delete(city_id):
        delete_city(city_id)
        return '', 204

    @staticmethod
    def post():
        parser.add_argument('name', type=str)
        args = parser.parse_args()
        return add_city(args['name'])

    @staticmethod
    def put(city_id):
        parser.add_argument('name', type=str)
        args = parser.parse_args()
        return update_city(city_id, args['name'])


class Cities(Resource):
    @staticmethod
    def get():
        data = get_cities()
        cities = []
        for record in data:
            cities.append({'id': record.city_id, 'name': record.city_name})
        return cities


api.add_resource(Cities, '/cities')
api.add_resource(City, '/city')
api.add_resource(City, '/city/<city_id>')

if __name__ == '__main__':
    app.run(debug=True)
