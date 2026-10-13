import logging
import os
from logging.config import fileConfig

from alembic import context
from flask import current_app
from sqlalchemy import text

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get('SCHEMA')

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

db = current_app.extensions['migrate'].db
config.set_main_option(
    'sqlalchemy.url',
    str(db.engine.url.render_as_string(hide_password=False)).replace('%', '%%'))
target_metadata = db.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode (emit SQL without a database)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""

    # Don't generate an empty migration when nothing changed
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    with db.engine.connect() as connection:
        # In production every table lives in its own schema
        if environment == "production":
            connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}"))
            connection.execute(text(f"SET search_path TO {SCHEMA}"))
            connection.commit()

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            **current_app.extensions['migrate'].configure_args)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
