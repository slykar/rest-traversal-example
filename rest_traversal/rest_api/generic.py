from spree import rest
from rest_traversal import db


class AlchemyCollection(rest.APICollection):

    query = None

    def create(self, request, deserialized):
        created = db.session.add(deserialized.data)
        db.session.flush()
        return created

    def retrieve(self, request):
        return self.query(request).run()


class AlchemyEntity(rest.APIEntity):
    model = None

    def update(self, request, deserialized):
        updated = db.session.merge(deserialized.data)
        db.session.flush()
        return updated

    def retrieve(self, request):
        return db.session.query(self.model).get(self.ref)
