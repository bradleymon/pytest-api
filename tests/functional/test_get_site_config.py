from apis import authenticate, siteconfiguration
from configs import config


#############################################################################
#
#   Feature:  A admin user (only) can retrieve site configuration from API
#
#############################################################################


def test_admin_gets_site_config():
    username = config.get('dispatcher_username')
    password = config.get('dispatcher_password')

    response = authenticate.post_authenticate(username, password)
    auth_token = response.json()['auth_token']
    json_site_config = siteconfiguration.get_siteconfiguration(auth_token)
    assert json_site_config['id'] > 0


# TODO
def test_customer_cannot_get_site_config():
    assert 1 == 1

