# coding=utf-8


class Address:
    """

    Класс, описывающий адрес доставки.

    """

    def __init__(self, city, street, house, building):
        self.city = city
        self.street = street
        self.house = house
        self.building = building
