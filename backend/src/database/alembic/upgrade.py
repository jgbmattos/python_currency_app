from alembic import command

from src.database.alembic.config import build_config


def upgrade(alembic_cfg):
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    upgrade(build_config())
