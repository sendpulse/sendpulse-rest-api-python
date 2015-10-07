# -*-coding:utf8-*-

""" SendPulse REST API usage example

Documentation:
    https://login.sendpulse.com/manual/rest-api/
    https://sendpulse.com/api
"""

from pysendpulse import PySendPulse

if __name__ == "__main__":
    REST_API_ID = ''
    REST_API_SECRET = ''
    TOKEN_STORAGE = 'memcached'
    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)

    # Get Mailing Lists list example
    SPApiProxy.get_list_of_addressbooks()

    # Send mail using SMTP
    email = {
        'subject': 'This is the test task from REST API',
        'html': '<h1>Hello, John!</h1><p>This is the test task from https://sendpulse.com/api REST API!</p>',
        'text': 'Hello, John!\nThis is the test task from https://sendpulse.com/api REST API!',
        'from': {'name': 'John Doe', 'email': 'john.doe@domain.com'},
        'to': [
            {'name': 'Jane Roe', 'email': 'jane.roe@domain.com'}
        ],
        'bcc': [
            {'name': 'Richard Roe', 'email': 'richard.roe@domain.com'}
        ]
    }
    SPApiProxy.smtp_send_mail(email)
