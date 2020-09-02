from contextlib import contextmanager

import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@contextmanager
def get_session():
    session = db.create_scoped_session(options=dict(bind=db.get_engine(flask.current_app, 'default'), binds={}))

    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


@contextmanager
def read_replica_async_session():
    session = db.create_scoped_session(options=dict(bind=db.get_engine(flask.current_app, 'default'), binds={}))

    try:
        yield session

    finally:
        session.close()
