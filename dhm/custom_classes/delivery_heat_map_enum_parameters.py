# coding=utf-8

from enum import Enum


class DeliveryHeatMapReportType(Enum):
    """

    Класс, необходимый для выбора типа отчета для построения тепловой карты.

    """
    DELIVERY_AMOUNT = 'По количеству доставок'.decode('utf-8')  # Число доставок
    DELIVERY_SUM = 'По суммарному чеку'.decode('utf-8')  # Суммарный чек
    AVG_CHEQUE = 'По среднему чеку'.decode('utf-8')  # Средний чек
    AVG_DELAY = 'По среднему времени опоздания'.decode('utf-8')
    MARKETING_SOURCE = 'По источнику рекламы'.decode('utf-8')
    PRODUCT_TYPE = 'По типу продукта'.decode('utf-8')

    @staticmethod
    def get_list():
        return [DeliveryHeatMapReportType.DELIVERY_AMOUNT,
                DeliveryHeatMapReportType.DELIVERY_SUM,
                DeliveryHeatMapReportType.AVG_CHEQUE,
                DeliveryHeatMapReportType.AVG_DELAY,
                DeliveryHeatMapReportType.MARKETING_SOURCE,
                DeliveryHeatMapReportType.PRODUCT_TYPE]


class DeliveryHeatMapPolygonSize(Enum):
    """

    Класс, необходимый для выбора размера стороны полигона тепловой карты в метрах.

    """
    ONE_HUNDRED_FIFTY = 150  # Размер полигона 150м х 150м
    THREE_HUNDRED = 300  # Размер полигона 300м х 300м
    FIVE_HUNDRED = 500  # Размер полигона 500м х 500м
    ONE_THOUSAND = 1000  # Размер полигона 1000м х 1000м
    FIVE_THOUSAND = 5000  # Размер полигона 5000м х 5000м
    FIFTEEN_THOUSAND = 15000  # Размер полигона 5000м х 5000м

    @staticmethod
    def get_list():
        return [DeliveryHeatMapPolygonSize.ONE_HUNDRED_FIFTY,
                DeliveryHeatMapPolygonSize.THREE_HUNDRED,
                DeliveryHeatMapPolygonSize.FIVE_HUNDRED,
                DeliveryHeatMapPolygonSize.ONE_THOUSAND,
                DeliveryHeatMapPolygonSize.FIVE_THOUSAND,
                DeliveryHeatMapPolygonSize.FIFTEEN_THOUSAND]

    # def get_as_str(self):
    #     if self == DeliveryHeatMapPolygonSize.ONE_HUNDRED_FIFTY:
    #         return '150 x 150 м'
    #     elif self == DeliveryHeatMapPolygonSize.THREE_HUNDRED:
    #         return '300 x 300 м'
    #     elif self == DeliveryHeatMapPolygonSize.FIVE_HUNDRED:
    #         return '500 x 500 м'
    #     elif self == DeliveryHeatMapPolygonSize.ONE_THOUSAND:
    #         return '1000 x 1000 м'
    #     elif self == DeliveryHeatMapPolygonSize.FIVE_THOUSAND:
    #         return '5 х 5 км'
    #     else:
    #         return '15 x 15 км'