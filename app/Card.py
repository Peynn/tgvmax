class Card(object):
    def __init__(cls, reference, number=None):
        cls.reference = reference
        cls.number = number

        if cls.reference == "SNCF.HappyCard" and cls.number is None:
            raise ValueError()
    
    def get_dict(cls):
        card = dict()
        card["reference"] = cls.reference
        
        if cls.number is not None:
            card["number"] = cls.number
        
        return card
