import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from dhm import controller
from dhm.custom_classes.delivery import DeliveryDTO


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def check_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'email' in body and 'password' in body:
            email = body['email']
            password = body['password']
        else:
            return HttpResponse(status=400, reason=['No email or password in request body'])

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        result = controller.check_user_credentials(email, password)
        if result['Success'] is False:
            if 'No user found with email' in result['Message']:
                return HttpResponse(status=404, reason=result['Message'])
            elif 'Wrong password:' in result['Message']:
                return HttpResponse(status=401, reason=result['Message'])
            return HttpResponse(status=500, reason=result['Message'])

    elif request.method == 'GET':
        pass
        # users = controller.get_all_users()
        # users_json = json.dumps(users)
        # return HttpResponse(users_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # email = body['email']
        # controller.delete_user(email)
    else:
        return HttpResponse(status=501, reason='Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'email' in body and 'password' in body and 'userName' in body:
            email = body['email']
            user_name = body['userName']
            password = body['password']
        else:
            return HttpResponse(status=400, reason=['No email, user name or password in request body'])

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        result = controller.safe_add_new_user(email, user_name, password)
        if result['Success'] is False:
            if 'Duplicate user email address' in result['Message']:
                return HttpResponse(status=409, reason=result['Message'])
            return HttpResponse(status=500, reason=result['Message'])

    elif request.method == 'GET':
        pass
        # users = controller.get_all_users()
        # users_json = json.dumps(users)
        # return HttpResponse(users_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # email = body['email']
        # controller.delete_user(email)
    else:
        return HttpResponse(status=501, reason='Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def reload_deliveries(request):

    print('here I am')
    return HttpResponse('Success request')


@csrf_exempt
def delivery(request):

    if request.method == 'POST':
        body = request.POST
        user_email = body['user']
        courier_name = body['courier']
        product_type = body['product_type']
        product = body['product']
        city = body['city']
        region = body['region']
        street = body['street']
        marketing_source = body['marketing_source']
        home = body['home']
        building = body['building']
        delivery_order_date_time = body['order_date_time']
        delivery_complete_date_time = body['complete_date_time']
        total_sum = body['total_sum']

        delivery_obj = DeliveryDTO.make_delivery(user_email,
                                                 courier_name,
                                                 product_type,
                                                 product,
                                                 city,
                                                 region,
                                                 street,
                                                 marketing_source,
                                                 home,
                                                 building,
                                                 delivery_order_date_time,
                                                 delivery_complete_date_time,
                                                 total_sum)

        result = controller.save_delivery(delivery_obj)
        if result['Success'] is False:
            if 'No user found with email address' in result['Message']:
                return HttpResponse(status=404, reason=result['Message'])
            return HttpResponse(status=500, reason=result['Message'])
    else:
        return HttpResponse(status=501, reason='Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def heat_map(request):

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'marketingSource' in body:
            marketing_source = body['marketingSource']
        else:
            marketing_source = None

        if 'productType' in body:
            product_type = body['productType']
        else:
            product_type = None

        map_filter = {
            'user_email': body['user'],
            'from_date': body['fromDate'],
            'to_date': body['toDate'],
            'report_type': body['reportType'],
            'marketing_source': marketing_source,
            'product_type': product_type,
            'polygon_size': body['polygonSize']
        }

        result = controller.calculate_heat_map(map_filter)

    else:
        return HttpResponse(status=501, reason='Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def filter_values(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']

        result = controller.get_all_filters(email)

        if result['Success'] is False:
            if 'No user found with email' in result['Message']:
                return HttpResponse(status=404, reason=result['Message'])
            elif 'Wrong password:' in result['Message']:
                return HttpResponse(status=401, reason=result['Message'])
            return HttpResponse(status=500, reason=result['Message'])

        result_json = json.dumps(result)
        return HttpResponse(result_json, content_type="application/json")

    elif request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return HttpResponse(status=501, reason='Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')
