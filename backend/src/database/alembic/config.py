from alembic.config import Config

from src.utils.settings import BASE_DIR, DB_URL


def get_db_url(db_url=None):
    if db_url:
        return db_url
    return DB_URL


def build_config(db_url=None):
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", f"{BASE_DIR}/database/alembic")
    if db_url:
        alembic_cfg.set_main_option("sqlalchemy.url", db_url)
        return alembic_cfg

    alembic_cfg.set_main_option("sqlalchemy.url", DB_URL)

    return alembic_cfg
