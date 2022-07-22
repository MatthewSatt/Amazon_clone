import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def login_notice():
    account_sid = "ACa2b799f6980f53da53b034ad127a1f33"
    auth_token = "86f8adee381fb8831f9de91d7426d8d2"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Amazon Login Alert!',
        from_='+15185203803',
        to='+17605858002')

