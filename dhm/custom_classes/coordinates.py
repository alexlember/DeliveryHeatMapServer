# coding=utf-8


class Coordinates:
    """

    Класс, описывающий пару координат широты и долготы для географического объекта.

    """

    # Координаты Москвы
    longitude = u'37.611347'
    latitude = u'55.760241'

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
