from .queries import OrderQuery
from rest_traversal import db, dbmodels
from rest_traversal.rest_api import generic

from .schemas import OrderSchema, OrderUpdateSchema


class OrderEntity(generic.AlchemyEntity):
    schema = OrderSchema
    update_schema = OrderUpdateSchema
    model = dbmodels.Order


class OrderList(generic.AlchemyCollection):
    endpoints = [
        (r'[0-9]+', OrderEntity)
    ]
    schema = OrderSchema
    query = OrderQuery
