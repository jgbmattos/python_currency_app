from src.database.helper import db
from src.utils.apm import apm
from src.utils.app_factory import build_app
from src.utils.routes import set_endpoints
from src.utils.settings import HOST, PORT, DEBUG

app = build_app()
apm.init_app(app)
db.init_app(app)
set_endpoints(app)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
