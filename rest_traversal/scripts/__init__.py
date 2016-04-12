import argparse
import sqlalchemy as sa
import transaction
from pyramid.paster import get_appsettings
from rest_traversal import db, dbmodels

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('config', help='INI configuration file')


def get_engine(config_uri: str) -> sa.engine.Engine:
    settings = get_appsettings(config_uri)
    return sa.engine_from_config(settings)


def init_db():
    args = parser.parse_args()
    engine = get_engine(args.config)
    db.metadata.drop_all(bind=engine)
    db.metadata.create_all(bind=engine)


def seed_db():
    from faker import Factory

    parser.add_argument('-n', '--number', type=int)
    args = parser.parse_args()

    fake = Factory.create()
    db.configure(get_appsettings(args.config))

    with transaction.manager:
        for n in range(0, args.number):
            customer = dbmodels.Customer(name=fake.company())
            for n2 in range(0, args.number):
                customer.offers.append(dbmodels.Offer(
                    amount=fake.pyint(),
                    created_at=fake.date_time_this_month()
                ))
            db.session.add(customer)
