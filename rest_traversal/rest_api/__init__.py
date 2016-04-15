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
    api = RentalAPI(request)
    return api
