from flask import Flask
from flask_restful import Resource, Api, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class SearchStation(Resource):
    def get(self):
        from app import Trainline

        args = request.args

        return Trainline.get_station(args['q'])

class Search(Resource):
    def post(self):
        from app import Trainline
        from app.Passenger import Passenger

        damien = Passenger(25)
        damien.add_card("SNCF.HappyCard", "HC900373024")
        passengers = [damien]

        json = request.get_json()
        departure_station_id = json["departure_station_id"]
        arrival_station_id = json["arrival_station_id"]
        departure_date = json["departure_date"]
        return_date = json["return_date"]
        # TODO : passengers

        return Trainline.search(
            departure_station_id,
            arrival_station_id,
            departure_date,
            return_date,
            passengers
        ).json()

api.add_resource(SearchStation, '/api/v1/stations')
api.add_resource(Search, '/api/v1/search')

if __name__ == '__main__':
    app.run(port=5002, debug=True)