from spree import filter
from rest_traversal import (
    db,
    dbmodels,
    queryobject as qo
)


class OrderQueryFilter(filter.Filter):
    order_by = filter.OrderBy(
        amount=dbmodels.Order.amount
    )


# noinspection PyClassHasNoInit
class OrderQuery(qo.QueryObject):

    filter = OrderQueryFilter

    def query(self, filter=None, *args, **kwargs):
        q = db.session.query(dbmodels.Order)
        if filter is not None:
            q = q.filter(filter)
        return q
