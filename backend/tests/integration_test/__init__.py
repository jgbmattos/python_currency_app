from src.database.helper import db
from src.models.base_model import BaseModel
from src.utils.app_factory import build_app
from src.utils.routes import set_endpoints


def build_testing_flask_app(db_uri):
    app = build_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_uri}"
    app.config['SQLALCHEMY_BINDS'] = {'default': f"sqlite:///{db_uri}"}

    app_context = app.app_context()
    app_context.push()
    db.init_app(app)
    BaseModel.metadata.create_all(db.get_engine())
    db.session.commit()
    set_endpoints(app)

    return app.test_client()
