import marshmallow
from marshmallow import fields as mf
from spree import rest

from .queries import OrderQuery
from rest_traversal import db, dbmodels
from rest_traversal.rest_api import generic


class NodeRef(mf.Field):
    """Field that takes the value from ``self.context['node'].ref``.
    It's only processed on load, a ``load_only`` parameter is forced,
    as well as ``missing`` parameter which is set to ``True``
    in order to always run the deserialization method.
    """
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'load_only': True,
            'missing': True,
            'required': True
        })
        super(NodeRef, self).__init__(*args, **kwargs)

    def _deserialize(self, value, attr, data):
        return self.context['node'].ref


class OrderUpdateSchema(marshmallow.Schema):

    id = NodeRef()
    created_at = mf.DateTime(dump_only=True)
    amount = mf.Integer(required=True)

    class Meta:
        additional = ('created_at',)

    @marshmallow.post_load
    def make_object(self, values):
        return dbmodels.Order(**values)


class OrderSchema(OrderUpdateSchema):
    id = mf.Integer()
    customer_id = mf.Integer()


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
