from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import BasicAuthAuthenticationPolicy
from rest_traversal import rest_api, db
import cornice

CUSTOMERS = {
    'super': {
        'customer_id': None,
        'password': 'duper',
        'group': 'admin'
    },
    'sly': {
        'customer_id': None,
        'password': 'zx8',
        'group': 'staff'
    },
    'daniel': {
        'customer_id': 1,
        'password': 'spree',
        'group': 'customers'
    }
}


def auth(username, password, request):
    if username not in CUSTOMERS:
        return None

    customer = CUSTOMERS[username]

    if customer['password'] != password:
        return None

    return [
        'c:{customer_id}'.format(**customer),
        'g:{group}'.format(**customer)
    ]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    db.configure(settings)
    config = Configurator(settings=settings, root_factory=rest_api.bootstrap)
    config.set_authentication_policy(BasicAuthAuthenticationPolicy(check=auth))
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_route('login', '/login')
    config.scan('rest_traversal')
    # Include REST Traversal views
    config.include('spree.rest')
    config.include('spree.rest.traversal.views')
    return config.make_wsgi_app()
