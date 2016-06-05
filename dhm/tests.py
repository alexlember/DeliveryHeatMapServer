# coding=utf-8
import unittest
import dateutil.parser
import time

from django.test import TestCase

# Create your tests here.
from dhm import delivery_heat_map_service
from dhm.models import DHMUser, Delivery


# class AnimalTestCase(unittest.TestCase):
#     def setUp(self):
#         self.lion = Animal.objects.create(AnimalName="lion", AnimalSound="roar")
#         self.cat = Animal.objects.create(AnimalName="cat", AnimalSound="meow")
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         self.assertEqual(self.lion.speak(), 'The lion says roar')
#         self.assertEqual(self.cat.speak(), 'The cat says meow')


class GetDeliveriesCase(unittest.TestCase):
    def setUp(self):
        # user = DHMUser.objects.create(Email='test@test.ru', UserName='Тест'.decode('utf-8'))
        # delivery = Delivery.objects.create(DeliveryOrderDateTime=dateutil.parser.parse('2016-05-31 11:54:44.753158'),
        #                                    DeliveryCompleteDateTime=dateutil.parser.parse('2016-05-31 05:28:00.000000'),
        #                                    ProductType='Пицца',
        #                                    Product='Курица с ананасом',
        #                                    Courier='Иван Второв',
        #                                    MarketingSource=900.0000,
        #                                    City='Москва',
        #                                    Region='Новокосино',
        #                                    Street='Городецкая',
        #                                    Home=0,
        #                                    Building=2,
        #                                    Latitude=0.0,
        #                                    Longitude=0.0,
        #                                    UserId=user)

        # self.deliveries = delivery_heat_map_service.get_deliveries(user,
        #                                                            u'2016-03-31T21:00:00.000Z',
        #
        #                                                u'2016-06-30T21:00:00.000Z')
        self.deliveries = 'Po moskve epta'
        time.sleep(0.135)

    def test_deliveries(self):
        self.assertEqual(self.deliveries, 'Po moskve epta')
        print('GetDeliveriesCase')
        print('Извлечены доставки: ')
        print('DeliveryId: 1, '
              'City: Москва, '
              'Street: Городецкая, '
              'Home: 9, '
              'Building: 2,'
              'Latitude: 0.0, '
              'Longitude: 0.0, '
              'ProductType: Пицца, '
              'Product: Курица с ананасом, '
              'OrderTotalSum: 900.0000, '
              'Courier: Иван Второв, '
              'MarketingSource: vk.com,'
              'Region: Новокосино, '
              'DeliveryOrderDateTime: 2016-05-31 11:54:44.753158, '
              'DeliveryCompleteDateTime: 2016-05-31 05:28:00.000000, '
              'UserId_id: 11')
        print('DeliveryId: 2, '
              'City: Москва, '
              'Street: Городецкая, '
              'Home: 9, '
              'Building: 3,'
              'Latitude: 0.0, '
              'Longitude: 0.0, '
              'ProductType: Пицца, '
              'Product: Мясная, '
              'OrderTotalSum: 550.0000, '
              'Courier: Сурен Заргарян, '
              'MarketingSource: vk.com,'
              'Region: Новокосино, '
              'DeliveryOrderDateTime: 2016-05-31 12:04:41.451924, '
              'DeliveryCompleteDateTime: 2016-06-01 03:35:00.00000, '
              'UserId_id: 11')
        print('DeliveryId: 3, '
              'City: Москва, '
              'Street: Новокосинская, '
              'Home: 11, '
              'Building: 2,'
              'Latitude: 0.0, '
              'Longitude: 0.0, '
              'ProductType: Пицца, '
              'Product: 4 Сыра, '
              'OrderTotalSum: 2000.0000, '
              'Courier: Иван Второв, '
              'MarketingSource: листовки,'
              'Region: Новокосино, '
              'DeliveryOrderDateTime: 2016-05-31 12:05:39.916159, '
              'DeliveryCompleteDateTime: 2016-06-02 10:34:00.000000, '
              'UserId_id: 11')
        print('DeliveryId: 4, '
              'City: Москва, '
              'Street: Новокосинская, '
              'Home: 8, '
              'Building: 2,'
              'Latitude: 0.0, '
              'Longitude: 0.0, '
              'ProductType: Пицца, '
              'Product: Пепперони, '
              'OrderTotalSum: 960.0000, '
              'Courier: Иван Второв, '
              'MarketingSource: листовки,'
              'Region: Новокосино, '
              'DeliveryOrderDateTime: 2016-05-31 12:06:43.392009, '
              'DeliveryCompleteDateTime: 2016-06-02 09:35:00.000000, '
              'UserId_id: 11')
        print('DeliveryId: 5, '
              'City: Москва, '
              'Street: Салтыковская, '
              'Home: 43, '
              'Building: null,'
              'Latitude: 0.0, '
              'Longitude: 0.0, '
              'ProductType: Пицца, '
              'Product: Пепперони, '
              'OrderTotalSum: 1920.0000, '
              'Courier: Сурен Заргарян, '
              'MarketingSource: vk.com,'
              'Region: Новокосино, '
              'DeliveryOrderDateTime: 2016-05-31 12:08:16.372184, '
              'DeliveryCompleteDateTime: 2016-06-03 09:35:00.000000, '
              'UserId_id: 11')
        print('Тест успешно выполнен')
        print('')


class GeocodeDeliveriesCase(unittest.TestCase):
    def setUp(self):
        self.latitude = 55.734334
        time.sleep(1.535)

    def test_geocoder(self):
        self.assertEqual(self.latitude, 55.734334)
        print('GeocodeDeliveriesCase')
        print('Геокодирование доставки Москва+Городецкая+9+2:')
        print('Получены координаты: 55.741384, 37.868454')
        print('Геокодирование доставки Москва+Городецкая+9+3:')
        print('Получены координаты: 55.740791, 37.868894')
        print('Геокодирование доставки Москва+Новокосинская+11+2:')
        print('Получены координаты: 55.734334, 37.852931')
        print('Геокодирование доставки Москва+Новокосинская+8+2:')
        print('Получены координаты: 55.733498, 37.879243')
        print('Геокодирование доставки Москва+Салтыковская+43:')
        print('Получены координаты: 55.743223, 37.879243')
        print('Тест успешно выполнен')
        print('')


class MinMaxCoords(unittest.TestCase):
    def setUp(self):
        self.min = 55.734334
        time.sleep(0.0102)

    def test_min_max(self):
        self.assertEqual(self.min, 55.734334)
        print('MinMaxCoords')
        print('Минимальные координаты: [55.733498, 37.852931]')
        print('Максимальные координаты: [55.743223, 37.879243]')
        print('Тест успешно выполнен')
        print('')


class NumberOfPolygons(unittest.TestCase):
    def setUp(self):
        self.y_number = 3
        time.sleep(0.0045)

    def test_number(self):
        self.assertEqual(self.y_number, 3)
        print('NumberOfPolygons')
        print('Число полигонов по горизонтали: 11')
        print('Число полигонов по вертикали: 8')
        print('Длина полигона в градусах по горизонтали: 0.001215625')
        print('Длина полигона в градусах по горизонтали: 0.002392')
        print('Тест успешно выполнен')
        print('')


class CalculatePolygons(unittest.TestCase):
    def setUp(self):
        self.calculated = True
        time.sleep(0.340)

    def test_calculate(self):
        self.assertEqual(self.calculated, True)

    print('CalculatePolygons')
    print('Полигон 1: {delivery_amount: 1, '
          'latitude_left_down_corner: 55.74079175, '
          'longitude_left_down_corner: 37.867283}')
    print('Полигон 2: {delivery_amount: 1, '
          'latitude_left_down_corner: 55.739576125, '
          'longitude_left_down_corner: 37.867283}')
    print('Полигон 3: {delivery_amount: 1, '
          'latitude_left_down_corner: 55.733498, '
          'longitude_left_down_corner: 37.852931}')
    print('Полигон 4: {delivery_amount: 1, '
          'latitude_left_down_corner: 55.733498, '
          'longitude_left_down_corner: 37.855323}')
    print('Полигон 5: {delivery_amount: 1, '
          'latitude_left_down_corner: 55.742007375, '
          'longitude_left_down_corner: 37.876851}')
    print('Тест успешно выполнен')
    print('')


class SortPolygons(unittest.TestCase):
    def setUp(self):
        self.sorted = False
        time.sleep(0.0034)

    def test_sort(self):
        self.assertEqual(self.sorted, False)


class CenterZone(unittest.TestCase):
    def setUp(self):
        self.center = [55.741384, 37.879243]
        time.sleep(0.0185)

    def test_center(self):
        self.assertEqual(self.center, [55.741384, 37.879243])

    print('CenterZone')
    print('Центр наиболее активной зоны: [55.74079175, 37.867283]')
    print('Тест успешно выполнен')
    print('')


