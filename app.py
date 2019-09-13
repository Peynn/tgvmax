import json

from app.Client import Client
from app.Passenger import Passenger
from utils import utils
from app import Trainline
from datetime import datetime, timedelta


def _get_trips(date, departure_station_id, arrival_station_id):
    damien = Passenger(25)
    damien.add_card("SNCF.HappyCard", "HC900373024")

    ret = Trainline.search(
        departure_station_id,
        arrival_station_id,
        str(date),
        None,
        [damien]
    )

    ret_json = ret.json()

    folders = ret_json['folders']
    stations = ret_json['stations']

    from utils import Colors
    import dateutil.parser

    for folder in folders:
        folder_id = folder['id']

        departure_station_id = utils._get_station_name(folder['departure_station_id'], stations)
        arrival_station_id = utils._get_station_name(folder['arrival_station_id'], stations)

        departure_date = utils._str_to_date(folder['departure_date'])
        arrival_date = utils._str_to_date(folder['arrival_date'])
        departure_day = utils._get_date_day(departure_date)
        departure_hours = utils._get_date_hours(departure_date)
        arrival_hours = utils._get_date_hours(arrival_date)

        cents = int(folder['cents'])
        subunit = int(folder['local_amount']['subunit_to_unit'])
        price = cents / subunit
        currency = folder['currency']

        color = None

        if cents == 0:
            color = Colors.RED

        trip_ids = folder['trip_ids']
        is_unsellable = False

        for trip in ret_json['trips']:
            if trip['id'] in trip_ids and 'short_unsellable_reason' in trip:
                is_unsellable = True
                break

        if is_unsellable == True:
            color = Colors.GRAY

        if color is not None:
            trip_str = departure_day + " " + departure_hours + " -> " + arrival_hours + " " + departure_station_id + " -> " + arrival_station_id

            if color == Colors.RED:
                send_mail(trip_str)
            
            Colors.cprint(
                color,
                trip_str,
                price, currency,
            )


def _get_station_loop(date, departure_station_id, arrival_station_id):
    import dateutil.parser

    for i in range(0, 1):
        _date = dateutil.parser.parse(date) + timedelta(hours=5 * i)
        _get_trips(_date, departure_station_id, arrival_station_id)

def send_mail(trip_str):
    import smtplib, ssl

    port = 465
    password = ""

    context = ssl.create_default_context()

    sender_email = "damien.trainline@gmail.com"
    receiver_email = "damien.vantourout@gmail.com"
    message = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender_email, receiver_email, trip_str, 'No message')
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == "__main__":
    import time

    while True:
        print('--------------------------------------------------')
        # Aix en provence 23614
        # Marseille 4790
        # Paris 4916
        # Antibes 5749
        # Avignon 485
        # Lyon 4718
        _get_station_loop("2019-08-16T06:00:00UTC", 5749, 4916)
        _get_station_loop("2019-08-17T06:00:00UTC", 5749, 4916)
        _get_station_loop("2019-08-17T06:00:00UTC", 4790, 4916)
        _get_station_loop("2019-08-17T06:00:00UTC", 23614, 4916)
        _get_station_loop("2019-08-17T06:00:00UTC", 485, 4916)
        _get_station_loop("2019-08-17T06:00:00UTC", 4718, 4916)
        _get_station_loop("2019-08-18T06:00:00UTC", 5749, 4916)
        _get_station_loop("2019-08-18T06:00:00UTC", 4790, 4916)
        _get_station_loop("2019-08-18T06:00:00UTC", 23614, 4916)
        _get_station_loop("2019-08-18T06:00:00UTC", 485, 4916)
        _get_station_loop("2019-08-17T06:00:00UTC", 4718, 4916)


        time.sleep(60 * 6)
    
