from spree import rest
from pyramid import security
from .customers import CustomerList
from .orders import OrderList


class RentalAPI(rest.APIEndpoint):

    __acl__ = [
        (security.Allow, security.Everyone, security.ALL_PERMISSIONS)
    ]

    def retrieve(self, request):
        return None

    def __init__(self, request):
        super(RentalAPI, self).__init__(
            parent=None,
            ref='root'
        )

    endpoints = [
        ('customers', CustomerList),
        ('orders', OrderList)
    ]


def bootstrap(request):
    """
    :type request: pyramid.request.Request
    :return:
    """

    """
    This is how a version switching could work based on QS ``v`` parameter,
    or url structure, so:

    `/v1/customers`     == `/customers?v=1`
    `/v2/customers`     == `/customers?v=2`

    Note that this allows you to do something like this:

    `/v2/customers?v=1` == `/v1/customers`
    """

    version = request.GET['v']

    api = RentalAPI(request)

    if version == '1':
        api = api['v1']
    elif version == '2':
        api = api['v2']

    return api
