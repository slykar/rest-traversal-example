import marshmallow
from marshmallow import fields
from rest_traversal import db, dbmodels, queryobject as qo
from spree import (
    filter as sf,
    rest
)

from pyramid import security


class OfferQueryFilter(sf.Filter):
    order_by = sf.fields.OrderBy(
        amount=dbmodels.Offer.amount
    )


# noinspection PyClassHasNoInit
class OfferQuery(qo.QueryObject):

    filter = OfferQueryFilter

    def query(self, filter=None, *args, **kwargs):
        q = db.session.query(dbmodels.Offer)
        if filter is not None:
            q = q.filter(filter)
        return q


class OfferSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'customer_id', 'amount', 'created_at')


class CustomerAcl(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def __call__(self):
        return [
            (security.Allow, 'c:{}'.format(self.customer_id), security.ALL_PERMISSIONS),
            (security.Deny, security.Everyone, security.ALL_PERMISSIONS)
        ]


class OfferList(rest.APICollectionEndpoint):

    @property
    def __acl__(self):
        return CustomerAcl(self.__parent__.ref)

    @staticmethod
    def serialize(offer_list):
        return OfferSchema(many=True).dump(offer_list).data

    def create(self, request):
        pass

    def retrieve(self, request):
        offer_query = OfferQuery(request)
        if isinstance(self.__parent__, Customer):
            # If it is a child of Customer, filter by customer refs
            return offer_query.run(dbmodels.Offer.customer_id == self.__parent__.ref)
        else:
            # Otherwise show all offers
            return offer_query.run()


class Offer(rest.APIEntityEndpoint):

    def retrieve(self):
        pass


class Customer(rest.APIEntityEndpoint):
    __name__ = 'customer'

    endpoints = [
        ('offers', OfferList)
    ]

    def retrieve(self, request):
        return db.session.query(dbmodels.Customer).get(self.ref)


class CustomerQueryFilter(sf.Filter):
    search = sf.fields.ILike(dbmodels.Customer.name)
    order_by = sf.fields.OrderBy(
        name=dbmodels.Customer.name
    )


# noinspection PyClassHasNoInit
class CustomerQuery(qo.QueryObject):

    filter = CustomerQueryFilter

    def query(self):
        return db.session.query(dbmodels.Customer)


class CustomerSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name')


class CustomerList(rest.APICollectionEndpoint):

    def create(self, request):
        pass

    __name__ = 'customers'

    endpoints = [
        (r'\d+', Customer),
    ]

    @staticmethod
    def serialize(customer_list):
        return CustomerSchema(many=True).dump(customer_list).data

    # noinspection PyMethodMayBeStatic
    def retrieve(self, request):
        return CustomerQuery(request).run()


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
        ('offers', OfferList)
    ]


def bootstrap(request):
    api = RentalAPI(request)
    return api
