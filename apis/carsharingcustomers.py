from loggings import logger
import requests
from configs import config

carsharingcustomers_url = config.get('base_url') + '/api/v2/carsharingcustomers'


def post_carsharingcustomer(email, password, phone_number):
    values = {'email': email,
              'password': password,
              'phone_number': phone_number}
    response = requests.post(carsharingcustomers_url, data=values)
    logger.logg("POST carsharingcustomers complete, status code: " + str(response.status_code))
    return response


def post_random_carsharingcustomer(customer):
    response = post_carsharingcustomer(customer.email, customer.password, customer.phone_number)
    return response


def patch_carsharingcustomer(customer, customer2):
    jwt_headers = {'Authorization': 'JWT {}'.format(customer.auth_token)}
    values = {"first_name": customer2.first_name,
              "last_name": customer2.last_name,
              "pin_number": customer2.pin_number}
    response = requests.patch(carsharingcustomers_url+"/"+str(customer.customer_id), data=values, headers=jwt_headers)
    logger.logg("PATCH carsharingcustomers complete, status code: " + str(response.status_code))
    return response
