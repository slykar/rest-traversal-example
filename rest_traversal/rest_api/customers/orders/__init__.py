from rest_traversal import dbmodels
from rest_traversal.rest_api.orders import OrderList
from ...orders import OrderQuery


class CustomerOrderList(OrderList):

    def retrieve(self, request):
        return OrderQuery(request).run(dbmodels.Order.customer_id == self.__parent__.ref)
