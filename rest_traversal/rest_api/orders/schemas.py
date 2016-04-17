import marshmallow
from marshmallow import fields

from spree import rest

from rest_traversal import dbmodels


class OrderUpdateSchema(marshmallow.Schema):

    id = rest.NodeRef()
    created_at = fields.DateTime(dump_only=True)
    amount = fields.Integer(required=True)

    class Meta:
        additional = ('created_at',)

    @marshmallow.post_load
    def make_object(self, values):
        return dbmodels.Order(**values)


class OrderSchema(OrderUpdateSchema):
    id = fields.Integer()
    customer_id = fields.Integer()