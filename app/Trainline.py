import json

from app.Client import Client


__client = Client()

def __get_passengers_dict(passengers):
    formated_passengers = []

    for passenger in passengers:
        formated_passengers.append(passenger.get_dict())
    
    return formated_passengers

def get_station(q_str):
    url = 'https://www.trainline.fr/api/v5_1/stations'
    params = {
        'context': 'search',
        'q': q_str
    }

    ret = __client._get(url, params=params)

    return ret.json()

def search(departure_station_id, arrival_station_id, departure_date, return_date, passengers):
    data = {
        "search": {
            "departure_date": departure_date,
            "return_date": return_date,
            "passengers": __get_passengers_dict(passengers),
            "systems": [
                "sncf",
                "db",
                "idtgv",
                "ouigo",
                "trenitalia",
                "ntv",
                "hkx",
                "renfe",
                "cff",
                "benerail",
                "ocebo",
                "westbahn",
                "leoexpress",
                "locomore",
                "busbud",
                "flixbus",
                "distribusion",
                "cityairporttrain",
                "obb",
                "timetable"
            ],
            "exchangeable_part": None,
            "source": None,
            "is_previous_available": None,
            "is_next_available": None,
            "departure_station_id": departure_station_id,
            "via_station_id": None,
            "arrival_station_id": arrival_station_id,
            "exchangeable_pnr_id": None
        }
    }

    ret = __client._post(
        url='https://www.trainline.fr/api/v5_1/search',
        data=json.dumps(data)
    )

    return ret
