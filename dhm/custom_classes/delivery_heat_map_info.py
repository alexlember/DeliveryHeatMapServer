# coding=utf-8

from json import JSONEncoder


class DeliveryHeatMapInfo(JSONEncoder):
    """

    Класс, описывающий объект тепловой карты со всеми необходимыми полями для ее построения.

    """

    def __init__(self, polygons, x_number_of_polygons, y_number_of_polygons, center_latitude_coordinate,
                 center_longitude_coordinate, color_range, min_latitude_coordinate, max_latitude_coordinate,
                 min_longitude_coordinate, max_longitude_coordinate, width, height):
        """

        Конструктор для создания объекта тепловой карты.

        :param polygons: Список со всеми полигонами.
        :param legend_values: Список элементов для отображения границ легенды.
        :param x_number_of_polygons: Число полигонов по горизонтали.
        :param y_number_of_polygons: Число полигонов по вертикали.
        :param center_latitude_coordinate: Серединная координаты широты всей зоны доставки.
        :param center_longitude_coordinate: Серединная координаты долготы всей зоны доставки.
        :param color_range: Количество полигонов одного цвета.
        :param min_latitude_coordinate: Минимальная координата широты.
        :param max_latitude_coordinate: Максимальная координата широты.
        :param min_longitude_coordinate: Минимальная координата долготы.
        :param max_longitude_coordinate: Максимальная координата долготы.
        :param width: Длина прямоугольника в градусах.
        :param height: Высота прямоугольника в градусах.
        :return: Объект, представляющий из себя тепловую карту.

        """

        super(DeliveryHeatMapInfo, self).__init__()
        self.polygons = polygons
        #self.legend_values = legend_values
        self.x_number_of_polygons = x_number_of_polygons
        self.y_number_of_polygons = y_number_of_polygons
        self.center_latitude_coordinate = center_latitude_coordinate
        self.center_longitude_coordinate = center_longitude_coordinate
        self.color_range = color_range
        self.min_latitude_coordinate = min_latitude_coordinate
        self.max_latitude_coordinate = max_latitude_coordinate
        self.min_longitude_coordinate = min_longitude_coordinate
        self.max_longitude_coordinate = max_longitude_coordinate
        self.width = width
        self.heigh = height

    def default(self, o):
        return o.__dict__
