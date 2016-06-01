# coding=utf-8
import json

import dateutil.parser
from django.core.exceptions import ObjectDoesNotExist
from flask import jsonify

from dhm import delivery_heat_map_service
from dhm.models import DHMUser, Delivery, DHMProductType, DHMMarketingSource
from pytz import timezone
from django.db.utils import IntegrityError

from dhm.custom_classes.delivery_heat_map_enum_parameters import DeliveryHeatMapReportType, DeliveryHeatMapPolygonSize


def safe_add_new_user(email, user_name, password):
    user = DHMUser(Email=email, UserName=user_name, Password=password)
    try:
        user.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate user email address: ' + email}
    return result


def check_user_credentials(email, password):

    try:
        user = DHMUser.objects.get(Email=email)
    except ObjectDoesNotExist:
        user = None

    if user is None:
        result = {'Success': False, 'Message': 'No user found with email address: ' + email}
    elif user.Password != password:
        result = {'Success': False, 'Message': 'Wrong password'}
    else:
        result = {'Success': True}

    return result


def calculate_heat_map(map_filter):

    try:
        user = DHMUser.objects.get(Email=map_filter['user_email'])
    except ObjectDoesNotExist:
        user = None

    if user is None:
        result = {'Success': False, 'Message': 'No user found with email address: ' + map_filter['user_email']}
    else:
        delivery_heat_map = delivery_heat_map_service.get_delivery_heat_map(user, map_filter)
        if delivery_heat_map['Success'] is False:
            result = {'Success': False, 'Message': delivery_heat_map['Message']}
        else:
            dhm_json = json.dumps(delivery_heat_map, default=lambda o: o.__dict__)
            result = {'Success': True, 'HeatMap': dhm_json}

    return result


def get_all_filters(email):

    try:
        user = DHMUser.objects.get(Email=email)
    except ObjectDoesNotExist:
        user = None

    if user is None:
        result = {'Success': False, 'Message': 'No user found with email address: ' + email}
    else:

        report_types = DeliveryHeatMapReportType.get_list()
        polygon_sizes = DeliveryHeatMapPolygonSize.get_list()
        marketing_sources = DHMMarketingSource.objects.filter(UserId=user).values('MarketingSourceName')
        product_types = DHMProductType.objects.filter(UserId=user).values('ProductTypeName')

        result = {'Success': True,
                  'reportTypes': report_types,
                  'polygonSizes': polygon_sizes,
                  'marketingSources': list(marketing_sources),
                  'productTypes': list(product_types)}

    return result


def save_delivery(delivery_obj):

    try:
        user_id = DHMUser.objects.get(Email=delivery_obj.user_email)
    except ObjectDoesNotExist:
        user_id = None

    if user_id is None:
        result = {'Success': False, 'Message': 'No user found with email address: ' + delivery_obj.user_email}
    else:
        delivery_order_date_time = dateutil.parser.parse(delivery_obj.delivery_order_date_time)

        delivery_complete_date_time = dateutil.parser.parse(delivery_obj.delivery_complete_date_time)

        delivery = Delivery(UserId=user_id,
                            DeliveryOrderDateTime=delivery_order_date_time,
                            DeliveryCompleteDateTime=delivery_complete_date_time,
                            ProductType=delivery_obj.product_type,
                            Product=delivery_obj.product,
                            Courier=delivery_obj.courier_name,
                            MarketingSource=delivery_obj.marketing_source,
                            OrderTotalSum=delivery_obj.total_sum,
                            City=delivery_obj.city,
                            Region=delivery_obj.region,
                            Street=delivery_obj.street,
                            Home=delivery_obj.home,
                            Building=delivery_obj.building,
                            Latitude=0.0,
                            Longitude=0.0)

        delivery.save()

        result = {'Success': True}

    return result
