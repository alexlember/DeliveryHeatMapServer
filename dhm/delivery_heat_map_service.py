# coding=utf-8

import datetime
import math

import datetime  # import datetime, timedelta
from datetime import timedelta

import dateutil.parser
import pytz
from pytz import timezone

from dhm.custom_classes.delivery_heat_map_enum_parameters import DeliveryHeatMapPolygonSize, DeliveryHeatMapReportType
from dhm.custom_classes.delivery_heat_map_info import DeliveryHeatMapInfo
from dhm.custom_classes.polygon_indexes import PolygonIndexes
from dhm.custom_classes.coordinates import Coordinates
from dhm.models import Delivery
from geocoder import geocode_deliveries, drop_coords
from dhm.custom_classes.delivery_polygon import DeliveryPolygon

"""Радиус Земли в метрах."""
EARTH_RADIUS = 6372795.0

"""Коэффициент для перевода градусов в радианы."""
RADIANS_PER_DEGREE = math.pi / 180

"""Число в градусах, приблизительно равное 500 метрам (для отрисовки 1 доставки)."""
DEGREES_IN_500_METERS = 0.001


def get_delivery_heat_map(user_id, map_filters):
    """

    Метод для формирования объекта тепловой карты.

    :param user_id: Идентификатор пользователя, для которого строится тепловая карта.
    :param date_from: Дата, начиная с которой следует включать доставки.
    :param date_to: Дата, по которую следует включать доставки.
    :param polygon_side_in_meters: Длина стороны полигона в метрах.
    :param report_type: Тип отчета для построения тепловой карты.
    :return: Объект тепловой карты.

    """

    deliveries = get_deliveries(user_id, map_filters['from_date'], map_filters['to_date'])

    #drop_coords(deliveries)

    geocode_deliveries(deliveries)

    min_max_coordinates = find_min_max_coordinates(deliveries)

    number_of_polygons_n_grid_step_in_degrees = calculate_number_of_polygons(map_filters['polygon_size'],
                                                                             min_max_coordinates)

    polygons = calculate_polygons(deliveries,
                                  map_filters['report_type'],
                                  number_of_polygons_n_grid_step_in_degrees,
                                  min_max_coordinates)

    sorted_polygons = polygons_sort_by_value(polygons)

    center_coordinates = calculate_center_coordinates(sorted_polygons)

    if center_coordinates is None:
        return {'Success': False, 'Message': 'No current polygons no center'}

    delivery_heat_map = DeliveryHeatMapInfo(sorted_polygons,
                                            number_of_polygons_n_grid_step_in_degrees['x_number_of_polygons'],
                                            number_of_polygons_n_grid_step_in_degrees['y_number_of_polygons'],
                                            center_coordinates.Latitude,
                                            center_coordinates.Longitude,
                                            4,
                                            float(min_max_coordinates['min_latitude']),
                                            float(min_max_coordinates['max_latitude']),
                                            float(min_max_coordinates['min_longitude']),
                                            float(min_max_coordinates['max_longitude']),
                                            float(number_of_polygons_n_grid_step_in_degrees['width']),
                                            float(number_of_polygons_n_grid_step_in_degrees['height']))

    return delivery_heat_map


def get_deliveries(user_id, date_from, date_to):
    """

    Метод извлекает все доставки указанного пользователя из БД.

    :param date_from: дата начала периода доставок
    :param date_to: дата окончания периода доставок
    :param user_id: идентификатор пользователя.
    :return deliveries: список доставок

    """
    date_from_parsed = dateutil.parser.parse(date_from)
    date_to_parsed = dateutil.parser.parse(date_to)

    valid_deliveries = Delivery.objects.filter(UserId=user_id,
                                               DeliveryCompleteDateTime__gt=datetime.date(date_from_parsed.year,
                                                                                          date_from_parsed.month,
                                                                                          date_from_parsed.day),
                                               DeliveryCompleteDateTime__lt=datetime.date(date_to_parsed.year,
                                                                                          date_to_parsed.month,
                                                                                          date_to_parsed.day))

    return list(valid_deliveries)


def find_min_max_coordinates(deliveries):
    """

    Метод находит максимальные и минимальные координаты широты и долготы всей зоны доставки.

    :param deliveries: Все доставки.
    :return min_max_coordinates: Словарь минимальных и максимальных широты и долготы.

    """

    max_latitude = -1.0
    min_latitude = 500.0
    max_longitude = -1.0
    min_longitude = 500.0

    # Прогон по всем доставкам и поиск границы зоны доставок по координатам.
    for delivery in deliveries:

        if delivery.Longitude is not None and delivery.Latitude is not None:

            if delivery.Latitude > max_latitude:
                max_latitude = delivery.Latitude
            if delivery.Latitude < min_latitude:
                min_latitude = delivery.Latitude
            if delivery.Longitude > max_longitude:
                max_longitude = delivery.Longitude
            if delivery.Longitude < min_longitude:
                min_longitude = delivery.Longitude

    min_max_coordinates = {'max_latitude': max_latitude,
                           'min_latitude': min_latitude,
                           'max_longitude': max_longitude,
                           'min_longitude': min_longitude}
    return min_max_coordinates


def calculate_number_of_polygons(polygon_side_in_meters, min_max_coordinates):
    """

    Метод находит число полигонов по вертикали и горизонтали и длины сторон полигонов в градусах.

    :param polygon_side_in_meters: Длина стороны полигона в метрах.
    :param min_max_coordinates: Посчитанные ранее макс и мин широта и долгота в зоне доставки.

    :return number_of_polygons_n_grip_step_in_degrees: Словарь с числом полигонов и с шагом сетки в градусах

    """

    min_coordinates = Coordinates(min_max_coordinates['min_longitude'], min_max_coordinates['min_latitude'])
    max_coordinates = Coordinates(min_max_coordinates['max_longitude'], min_max_coordinates['max_latitude'])

    # Вычисление расстояния между двумя точками в метрах.
    x_size_in_meters = calculate_distance_between_two_points(min_coordinates.Latitude,
                                                             min_coordinates.Longitude,
                                                             min_coordinates.Latitude,
                                                             max_coordinates.Longitude)

    y_size_in_meters = calculate_distance_between_two_points(min_coordinates.Latitude,
                                                             min_coordinates.Longitude,
                                                             max_coordinates.Latitude,
                                                             min_coordinates.Longitude)

    # Вычисление количества прямоугольников по горизонтали и по вертикали.
    if x_size_in_meters != 0.0:
        x_number_of_polygons = int((x_size_in_meters // int(polygon_side_in_meters) + 1))
    else:
        x_number_of_polygons = 0

    if y_size_in_meters != 0.0:
        y_number_of_polygons = int((y_size_in_meters // int(polygon_side_in_meters) + 1))
    else:
        y_number_of_polygons = 0

    # Установка шага сетки в градусах.
    if x_number_of_polygons > 0 and y_number_of_polygons > 0:
        width = (max_coordinates.Longitude - min_coordinates.Longitude) / x_number_of_polygons
        height = (max_coordinates.Latitude - min_coordinates.Latitude) / y_number_of_polygons
    else:
        width = DEGREES_IN_500_METERS * 2
        height = DEGREES_IN_500_METERS

    number_of_polygons_n_grip_step_in_degrees = {'x_number_of_polygons': x_number_of_polygons,
                                                 'y_number_of_polygons': y_number_of_polygons,
                                                 'width': width,
                                                 'height': height}
    return number_of_polygons_n_grip_step_in_degrees


def calculate_distance_between_two_points(start_latitude, start_longitude, finish_latitude, finish_longitude):
    """

    Метод для вычисления расстояния в метрах между двумя точками.

    :param start_latitude: Начальная широта.
    :param start_longitude: Начальная долгота.
    :param finish_latitude: Конечная широта.
    :param finish_longitude: Конечная долгота.
    :return distance: расстояние между точками в метрах.

    """

    # Сферическая теорема косинусов.
    angular_distance = math.acos(
        math.sin(float(start_latitude) * RADIANS_PER_DEGREE) *
        math.sin(float(finish_latitude) * RADIANS_PER_DEGREE) +
        math.cos(float(start_latitude) * RADIANS_PER_DEGREE) *
        math.cos(float(finish_latitude) * RADIANS_PER_DEGREE) *
        math.cos(float((start_longitude - finish_longitude)) * RADIANS_PER_DEGREE))

    # Перевод углового расстояния в метры.
    return angular_distance * EARTH_RADIUS


def calculate_polygons(deliveries, report_type, number_of_polygons_n_grip_step_in_degrees, min_max_coordinates):
    """

    Метод для формирования коллеции полигонов.

    :param min_max_coordinates: Словарь с макс и мин координатами зоны доставки
    :param number_of_polygons_n_grip_step_in_degrees: число полигонов и шаг сетки
    :param deliveries: доставки, которые участвуют в формировании
    :param report_type: тип отчета

    :return polygons: список полигонов

    """

    min_latitude = float(min_max_coordinates['min_latitude'])
    min_longitude = float(min_max_coordinates['min_longitude'])
    x_number_of_polygons = number_of_polygons_n_grip_step_in_degrees['x_number_of_polygons']
    y_number_of_polygons = number_of_polygons_n_grip_step_in_degrees['y_number_of_polygons']
    x_step = float(number_of_polygons_n_grip_step_in_degrees['width'])
    y_step = float(number_of_polygons_n_grip_step_in_degrees['height'])

    """
    Словарь для полигонов, уникальный ключ - пара: порядковый номер полигона по вертикали и по горизонтали,
    отсчитывая от нижнего левого угла зоны доставки.
    """
    polygons_map = dict()

    """
    Алгоритм нахождения положения точки доставки (включение ее в какой-либо полигон):
    на всей территории доставок строится виртуальная сетка из полигонов, с заданным шагом (xStep, yStep).
    У каждой доставки известны координаты, т.е. если взять отступ доставки в координатах
    от левого нижнего угла зоны доставок и разделить его на шаг сетки (высоту или ширину полигона в координатах),
    то найдем порядковый номер полигона по горизонтали (если поделим longitude - высоту)
    и по вертикали (если поделим latitude - ширину). Пара номеров по горизонтали и по вериткали - уникальный ключ.
    Осуществляется попытка поиска полигона по порядковому номеру как по уникальному ключу в мапе, если такой
    находится, то число доставок у него увеличивается, а если в мапе элемента нет,
    то он добавляется туда и число доставок устанавливается в 1.
    """
    for delivery in deliveries:
        if delivery.Latitude is not None and delivery.Longitude is not None:

            # Cмещение долготы конкретной доставки от крайней левой точки.
            x_shift = float(delivery.Longitude) - min_longitude

            # Cмещение широты конкретной доставки от крайней нижней точки.
            y_shift = float(delivery.Latitude) - min_latitude

            # Текущий номер полигона по горизонтали.
            x_current_polygon = int(x_shift // x_step)

            # Текущий номер полигона по вертикали.
            y_current_polygon = int(y_shift // y_step)

            # Проверка невыхода индексов за рамки массива.
            if x_current_polygon == x_number_of_polygons:
                x_index = x_current_polygon - 1
            else:
                x_index = x_current_polygon

            if y_current_polygon == y_number_of_polygons:
                y_index = y_current_polygon - 1
            else:
                y_index = y_current_polygon

            key = PolygonIndexes(x_index, y_index)

            """
            Если мапа не содержит полигон с такой парой номеров по горизонтали и вертикали -
            вычисляем координаты его левого нижнего угла и добавляем в мапу.
            """
            if key not in polygons_map:
                left_down_corner_longitude = min_longitude + x_index * x_step
                left_down_corner_latitude = min_latitude + y_index * y_step
                polygon = DeliveryPolygon(0, 0, left_down_corner_latitude, left_down_corner_longitude)
                polygons_map[key] = polygon

            # Если такой полигон уже есть в мапе, то просто переходим к вычислению необходимой величины для отчета.
            polygon_process(polygons_map, key, report_type, delivery)

    if report_type == DeliveryHeatMapReportType.AVG_CHEQUE:
        for key in polygons_map:
            polygons_map[key].value /= polygons_map[key].delivery_amount

    return polygons_map


def polygon_process(polygons_map, key, report_type, delivery):
    """

    Метод подсчитывает необходимые величины для полигона в зависимости от типа отчета и кладет в словарь.

    :param polygons_map: Словарь с полигонами.
    :param key: Ключ для поиска нужного полигона.
    :param report_type: Тип отчета для построения тепловой карты.
    :param delivery: Текущая доставка.

    """

    polygon = polygons_map[key]

    if report_type == DeliveryHeatMapReportType.DELIVERY_AMOUNT:
        polygon.increment_delivery_amount()
        polygon.value += 1
    elif report_type == DeliveryHeatMapReportType.DELIVERY_SUM:
        polygon.add_to_value(delivery.total_sum)
    else:
        polygon.increment_delivery_amount()
        polygon.add_to_value(delivery.total_sum)


def polygons_sort_by_value(polygons):
    """

    Метод необходим для сортировки словаря полигонов по полю value.

    :param polygons: Словарь из полигонов.
    :return: Список полигонов, отсортированный по value

    """

    sorted_polygons = sorted(polygons.values(), key=lambda polygon: polygon.value, reverse=True)
    return sorted_polygons


def calculate_center_coordinates(polygons):
    """
    Метод для нахождения центра зоны доставки. Берется как полигон с наибольшим значением value.

    :param sorted_polygons: Список с полигонами.
    :return center_coordinates: Пара центральных координат зоны доставки.

    """
    if len(polygons) > 0:
        center_coordinates = Coordinates(polygons[0].longitude_left_down_corner,
                                         polygons[0].latitude_left_down_corner)
        return center_coordinates
    else:
        return None


# get_delivery_heat_map(1,
#                       datetime.datetime(2015, 11, 10),  # 14, 15, 59, 999999, tzinfo=None),
#                       datetime.datetime(2016, 01, 10),  # 14, 15, 59, 999999, tzinfo=None),
#                       DeliveryHeatMapPolygonSize.FIVE_HUNDRED,
#                       DeliveryHeatMapReportType.DELIVERY_AMOUNT)
