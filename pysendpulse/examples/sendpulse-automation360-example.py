# -*-coding:utf8-*-

"""
SendPulse Automation360 usage example
"""

from pysendpulse.automation360 import Automation360

eventHash = 'e5a0e6aa4abd4d43a9a28cbff32c2515/6741804'
variables = dict(
    user_id=1231231,
    firstName="Name",
    lastName="Family",
    age=23)
email = 'email@domain.com'
phone = '380931112233'

# if empty email or phone
# phone = None
# or
# email = None
automationClient = Automation360(eventHash)
result = automationClient.send_event_to_sendpulse(email, phone, variables)

print(result)
