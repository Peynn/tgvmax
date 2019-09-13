def _str_to_date(date):
    import dateutil.parser

    date = dateutil.parser.parse(date)

    return date

def _get_date_day(date):
    date_str = date.strftime('%d/%m')
    
    return date_str

def _get_date_hours(date):
    date_str = date.strftime('%H:%M')

    return date_str

def _get_station_name(station_id, stations):
    for station in stations:
        if station['id'] == station_id:
            return station['name']
