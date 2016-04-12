from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import BasicAuthAuthenticationPolicy
from rest_traversal import rest_api, db


CUSTOMERS = {
    'sly': {
        'customer_id': 1,
        'password': 'zx8'
    },
    'daniel': {
        'customer_id': 2,
        'password': 'spree'
    }
}


def auth(username, password, request):
    if username not in CUSTOMERS:
        return None

    customer = CUSTOMERS[username]

    if customer['password'] != password:
        return None

    return [
        'c:{}'.format(customer['customer_id'])
    ]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    db.configure(settings)
    config = Configurator(settings=settings, root_factory=rest_api.bootstrap)
    config.set_authentication_policy(BasicAuthAuthenticationPolicy(check=auth))
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_route('login', '/login')
    config.scan('rest_traversal.views')
    # TODO create an include option
    config.include('spree.rest.traversal.view')
    return config.make_wsgi_app()
