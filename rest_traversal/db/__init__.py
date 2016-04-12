import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
":type session: sqlalchemy.orm.session.Session or scoped_session"

engine = None

metadata = sa.MetaData()

Base = declarative_base(metadata=metadata)


def configure(settings):
    global engine
    engine = sa.engine_from_config(settings, client_encoding='utf-8')
    metadata.bind = engine
    session.configure(bind=engine)
