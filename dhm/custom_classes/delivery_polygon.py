# coding=utf-8


class DeliveryPolygon:
    """

    Класс, описывающий полигон, который будет отображен на тепловой карте.

    """

    def __init__(self, delivery_amount, value, latitude_left_down_corner, longitude_left_down_corner):
        """

        Конструктор, инициализирующий объект полигона.

        :param delivery_amount: Число доставок, попадающих в заданный квадрат.
        :type delivery_amount: int
        :param value: Величина, которая может использоваться по разному (как общая сумма заказа, средняя сумма заказа,
                      число доставок, среднее время опоздания), в зависимости от типа отчета.
        :type value: float
        :param latitude_left_down_corner: Координата широты левого нижнего угла.
        :type latitude_left_down_corner: float
        :param longitude_left_down_corner: Координата долготы левого нижнего угла.
        :type longitude_left_down_corner: float

        """
        self.delivery_amount = delivery_amount
        self.value = value
        self.latitude_left_down_corner = latitude_left_down_corner
        self.longitude_left_down_corner = longitude_left_down_corner

    def increment_delivery_amount(self):
        """

        Метод для увеличения числа доставок полигона на 1.

        """
        self.delivery_amount += 1

    def add_to_value(self, additional_value):
        """

        Метод добавляет величину к универсальному поля value.

        :param additional_value: величина, на которую увеличится значение self.value
        :type additional_value: float

        """

        self.value += additional_value
