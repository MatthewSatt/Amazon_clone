import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # TWILIO_ACCOUNT_SID=os.environ.get('TWILIO_ACCOUNT_SID')
    # TWILIO_AUTH_TOKEN= os.environ.get('TWILIO_AUTH_TOKEN')
    # TWILIO_NUMBER = os.environ.get('+15185203803')
    # SQLAlchemy 1.4 no longer supports url strings that start with 'postgres'
    # (only 'postgresql') but heroku's postgres add-on automatically sets the
    # url in the hidden config vars to start with postgres.
    # so the connection uri must be updated here
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_ECHO = True
