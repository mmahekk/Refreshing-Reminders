import os
import threading
from time import sleep

from twilio.rest import Client

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_water_reminder(client, recipient_number, recipient_name):
    water_reminder = """
        Hey {}, this is your reminder to take a sip of water!""".format(recipient_name)

    try:
        message = client.messages.create(
            body = water_reminder,
            from_= '+19282720782',  # This is the Twilio Sandbox number. Don't change it.
            to=recipient_number
        )

        print("Water reminder sent to", recipient_name, "on SMS number", recipient_number)
        sleep(5)
        send_water_reminder(client, recipient_number, recipient_name)

    except Exception as e:
        print("Something went wrong. Water reminder message not sent.")
        print(repr(e))

def send_vitamin_reminder(client, recipient_number, recipient_name):
    vitamin_reminder = """
        Hey {}, this is your reminder to take all your vitamins!""".format(recipient_name)

    try:
        message = client.messages.create(
            body = vitamin_reminder,
            from_= '+19282720782',  # This is the Twilio Sandbox number. Don't change it.
            to=recipient_number
        )

        print("Vitamin reminder sent to", recipient_name, "on SMS number", recipient_number)
        sleep(7)
        send_vitamin_reminder(client, recipient_number, recipient_name)

    except Exception as e:
        print("Something went wrong. Vitamin reminder message not sent.")
        print(repr(e))


threading.Timer(1.0, send_water_reminder, args=[client, '+1##########', 'Jaya']).start()
threading.Timer(1.0, send_vitamin_reminder, args=[client, '+1##########', 'Jaya']).start()
