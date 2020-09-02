from alembic import command

from src.database.alembic.config import build_config


def revision(alembic_cfg):
    command.revision(alembic_cfg, autogenerate=True)


if __name__ == "__main__":
    revision(build_config())
