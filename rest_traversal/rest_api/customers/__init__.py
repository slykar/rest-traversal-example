import marshmallow
from pyramid import security

from spree import rest, filter

from rest_traversal import dbmodels, db, queryobject as qo
from .. import acl
from .orders import CustomerOrderList


class CustomerAcl(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def __call__(self):
        return [
            (security.Allow, 'c:{}'.format(self.customer_id), security.ALL_PERMISSIONS),
            (security.Deny, security.Everyone, security.ALL_PERMISSIONS)
        ]


class CustomerSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name')


class CustomerEntity(rest.APIEntityEndpoint):
    schema = CustomerSchema
    endpoints = [
        ('orders', CustomerOrderList)
    ]

    def update(self, request):
        pass

    def retrieve(self, request):
        return db.session.query(dbmodels.Customer).get(self.ref)


class CustomerQueryFilter(filter.Filter):
    search = filter.ILike(dbmodels.Customer.name)
    order_by = filter.OrderBy(
        name=dbmodels.Customer.name
    )


# noinspection PyClassHasNoInit
class CustomerQuery(qo.QueryObject):

    filter = CustomerQueryFilter

    def query(self):
        return db.session.query(dbmodels.Customer)


class CustomerList(rest.APICollectionEndpoint):

    schema = CustomerSchema
    endpoints = [
        (r'\d+', CustomerEntity),
    ]

    @property
    def __acl__(self):
        return acl.StaffAcl()

    def create(self, request, serialized):
        pass

    # noinspection PyMethodMayBeStatic
    def retrieve(self, request):
        return CustomerQuery(request).run()
