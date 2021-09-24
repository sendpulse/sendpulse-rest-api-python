# -*- encoding:utf8 -*-

"""
Wrapper for interacting with SendPulse Automation 360
"""

import requests
import logging

try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        try:
            from django.utils import simplejson as json
        except ImportError:
            raise ImportError('A json library is required to use this python library')

logger = logging.getLogger(__name__)
logger.propagate = False
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(levelname)-8s [%(asctime)s]  %(message)s'))
logger.addHandler(ch)


class Automation360:
    eventsHash = None
    eventDomain = 'https://events.sendpulse.com/events/id/'

    def __init__(self, eventHash):
        self.eventsHash = eventHash

    def send_event_to_sendpulse(self, email, phone, variables):
        if not email and not phone:
            raise Exception('Email and phone is empty')
        if email:
            variables['email'] = email
        if phone:
            variables['phone'] = phone
        result = self.__send_request(variables)
        return result

    def __send_request(self, variables):
        url = self.eventDomain + self.eventsHash
        logger.debug("__send_request: url: '{}' with variables: {}".format(url, variables))
        variables = json.dumps(variables)
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.post(url, headers=headers, data=variables)
        if response.status_code != 200:
            logger.debug("Raw_server_response: {}".format(response.text))
        return response
