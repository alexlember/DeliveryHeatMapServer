# coding=utf-8

from __future__ import print_function
import json

import requests
from dhm.custom_classes.coordinates import Coordinates
from dhm.custom_classes.address import Address


def geocode_deliveries(deliveries):
    """

    Метод производит геокодирование для тех доставок, у которых нет координат.

    :param deliveries: список доставок для геокодирования.
    :return: обновляет доставки в БД.

    """

    for delivery in deliveries:
        if delivery.latitude is None \
           or delivery.longitude is None \
           or delivery.latitude == 0.0 \
           or delivery.longitude == 0.0:
            coords = get_coords(Address(delivery.city, delivery.street, delivery.house, delivery.building))
            delivery.longitude = coords.longitude
            delivery.latitude = coords.latitude


def get_coords(delivery_address):
    """

    Метод образается к Yandex API и получает точные координаты по адресу.

    :param delivery_address: Адрес, который необходимо геокодировать.
    :return: Объект координат адреса.

    """
    params = delivery_address.city + "+" + delivery_address.street + "+" + str(delivery_address.house)

    if delivery_address.building is not None:
        params += str(delivery_address.building)

    url = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode=' + params

    result = requests.get(url)
    json_string = json.loads(result.content)

    json_dict = json_string['response']['GeoObjectCollection']['featureMember']
    object_coords = json_dict[0]['GeoObject']['Point']['pos']
    splitted_coords = object_coords.split()
    longitude = (float)(splitted_coords[0].encode('utf-8'))
    latitude = (float)(splitted_coords[1].encode('utf-8'))

    # print "longitude: %s, latitude: %s" % (repr(longitude), repr(latitude))
    print("ok")

    return Coordinates(longitude, latitude)
