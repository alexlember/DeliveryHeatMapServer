# coding=utf-8


class Coordinates:
    """

    Класс, описывающий пару координат широты и долготы для географического объекта.

    """

    # Координаты Москвы
    Longitude = u'37.611347'
    Latitude = u'55.760241'

    def __init__(self, longitude, latitude):
        self.Longitude = longitude
        self.Latitude = latitude
