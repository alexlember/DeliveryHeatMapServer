# coding=utf-8
import unittest
import dateutil.parser

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
        user = DHMUser.objects.create(Email='test@test.ru', UserName='Тест')
        delivery = Delivery.objects.create(DeliveryOrderDateTime=dateutil.parser.parse('2016-05-31 11:54:44.753158'),
                                           DeliveryCompleteDateTime=dateutil.parser.parse('2016-05-31 05:28:00.000000'),
                                           ProductType='Пицца',
                                           Product='Курица с ананасом',
                                           Courier='Иван Второв',
                                           MarketingSource=900.0000,
                                           City='Москва',
                                           Region='Новокосино',
                                           Street='Городецкая',
                                           Home=0,
                                           Building=2,
                                           Latitude=0.0,
                                           Longitude=0.0,
                                           UserId=user)

        self.deliveries = delivery_heat_map_service.get_deliveries(user,
                                                                   u'2016-03-31T21:00:00.000Z',
                                                                   u'2016-06-30T21:00:00.000Z')

    def test_deliveries(self):
        print ('lala')
        pass
