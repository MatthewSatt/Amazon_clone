FROM node:22-alpine AS build-stage

WORKDIR /react-app

# Install dependencies first so they're cached between builds
COPY react-app/package.json react-app/package-lock.json ./
RUN npm ci

# Build our React App
COPY react-app/ .
RUN npm run build


FROM python:3.12-slim

# Setup Flask environment
ENV FLASK_APP=app \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /var/www

# Install Python Dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .flaskenv ./
COPY app app
COPY migrations migrations
# Flask serves the React build from ../react-app/dist (see app/__init__.py)
COPY --from=build-stage /react-app/dist react-app/dist
COPY docker-entrypoint.sh /usr/local/bin/

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# Migrate (and seed an empty database) before starting the server
ENTRYPOINT ["docker-entrypoint.sh"]

# Hosts like Heroku/Render provide $PORT; default to 8000.
CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-8000} --workers ${WEB_CONCURRENCY:-2} app:app"]
