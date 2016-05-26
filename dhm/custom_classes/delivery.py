class DeliveryDTO(object):
    user_email = ""
    courier_name = ""
    product_type = ""
    product = ""
    city = ""
    region = ""
    street = ""
    marketing_source = ""
    home = 1
    building = 1
    delivery_order_date_time = ""
    delivery_complete_date_time = ""
    total_sum = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self,
                 user_email,
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
                 total_sum):
        self.user_email = user_email
        self.courier_name = courier_name
        self.product_type = product_type
        self.product = product
        self.city = city
        self.region = region
        self.street = street
        self.marketing_source = marketing_source
        self.home = home
        self.building = building
        self.delivery_order_date_time = delivery_order_date_time
        self.delivery_complete_date_time = delivery_complete_date_time
        self.total_sum = total_sum

    @staticmethod
    def make_delivery(user_email,
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
                      total_sum):
        delivery_obj = DeliveryDTO(user_email, courier_name, product_type,
                                   product, city, region, street,
                                   marketing_source, home, building, delivery_order_date_time,
                                   delivery_complete_date_time, total_sum)
        return delivery_obj
