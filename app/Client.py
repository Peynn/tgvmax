import requests


class Client:
    def __init__(cls):
        cls.session = requests.session()

        cls.headers = {
            'Accept': 'application/json',
            'Accept-Language': 'fr',
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'www.trainline.eu',
            'User-Agent': 'CaptainTrain/43(4302) Android/4.4.2(19)'
        }
    
    def _get(cls, url, params=None):
        ret = cls.session.get(url=url, headers=cls.headers, params=params)

        return ret
    
    def _post(cls, url, data):
        ret = cls.session.post(url=url, headers=cls.headers, data=data)

        return ret
