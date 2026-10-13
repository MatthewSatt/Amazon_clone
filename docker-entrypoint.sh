#!/bin/sh
set -e

flask db upgrade

# Seed demo data only on first start, while there are no users yet
if python -c "
from app import app
from app.models import User, db
with app.app_context():
    raise SystemExit(1 if db.session.scalar(db.select(User.id).limit(1)) else 0)
"; then
    flask seed all
fi

exec "$@"
