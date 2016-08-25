import datetime
import sqlalchemy as sa
from sqlalchemy import orm
from rest_traversal import db


class Customer(db.Base):
    __tablename__ = 'api_customers'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), unique=True)


class Order(db.Base):
    __tablename__ = 'api_orders'
    id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey(Customer.id))
    amount = sa.Column(sa.Integer, nullable=False)
    paid = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(
        sa.DateTime(),
        nullable=False,
        default=datetime.datetime.now,
        server_default=sa.func.now()
    )

    # ===== Relations =====

    customer = orm.relationship(Customer, backref='orders')
