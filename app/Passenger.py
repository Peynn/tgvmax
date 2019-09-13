from app.Card import Card
import uuid


class Passenger(object):
    def __init__(cls, age):
        cls.id = cls.gen_id()
        cls.age = age
        cls.cards = []
    

    def add_card(cls, reference, number=None):
        cls.cards.append(
            Card(
                reference,
                number
            )
        )
    
    def gen_id(cls):
        return str(uuid.uuid4())
    
    def get_dict(cls):
        data = {
            "id": cls.id,
            "label": "youth",
            "age": cls.age,
            "cards": cls.get_cards_dict(),
            "cui": None
        }

        return data

    def get_cards_dict(cls):
        cards = []

        for card in cls.cards:
            cards.append(card.get_dict())
        
        return cards
