from spree import rest

from .queries import OrderQuery
from rest_traversal import db, dbmodels
from rest_traversal.rest_api import generic

from .schemas import OrderSchema, OrderUpdateSchema


class OrderMarkAction(rest.APIAction):

    def put(self, request, data):
        order = dbmodels.Order(
            id=self.__parent__.ref,
            paid=True
        )
        return OrderSchema().dump(db.session.merge(order))

    def delete(self, request, data):
        order = dbmodels.Order(
            id=self.__parent__.ref,
            paid=False
        )
        return OrderSchema().dump(db.session.merge(order))


class OrderEntity(generic.AlchemyEntity):
    schema = OrderSchema
    update_schema = OrderUpdateSchema
    model = dbmodels.Order

    endpoints = [
        ('paid', OrderMarkAction)
    ]


class OrderList(generic.AlchemyCollection):
    endpoints = [
        (r'[0-9]+', OrderEntity)
    ]
    schema = OrderSchema
    query = OrderQuery

    def after_create(self, request, created, deserialized):
        pass
