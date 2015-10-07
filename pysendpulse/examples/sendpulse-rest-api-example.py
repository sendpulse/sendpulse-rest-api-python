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

    # Get balance in Japanese Yen
    SPApiProxy.get_balance('JPY')

    # Get Mailing Lists list example
    SPApiProxy.get_list_of_addressbooks()

    # Get Mailing Lists list with limit and offset example
    SPApiProxy.get_list_of_addressbooks(offset=5, limit=2)

    # Add emails with variables to addressbook
    emails_for_add = [
        {
            'email': 'test1@test1.com',
            'variables': {
                'name': 'test11',
                'number': '11'
            }
        },
        {'email': 'test2@test2.com'},
        {
            'email': 'test3@test3.com',
            'variables': {
                'firstname': 'test33',
                'age': 33,
                'date': '2015-09-30'
            }
        }
    ]
    SPApiProxy.add_emails_to_addressbook(ADDRESSBOOK_ID, emails_for_add)

    # Delete email from addressbook
    emails_for_delete = ['test4@test4.com']
    SPApiProxy.delete_emails_from_addressbook(ADDRESSBOOK_ID, emails_for_delete)

    # Add sender "FROM" email
    SPApiProxy.add_sender('jane.roe@domain.com', 'Jane Roe')

    # Get list of senders
    SPApiProxy.get_list_of_senders()

    # Add emails to unsubscribe list
    SPApiProxy.smtp_add_emails_to_unsubscribe([
        {'email': 'test_1@domain_1.com', 'comment': 'comment_1'},
        {'email': 'test_2@domain_2.com', 'comment': 'comment_2'}
    ])

    # Create new email campaign with attaches
    task_body = "<h1>Hello, John!</h1><p>This is the test task from https://sendpulse.com/api REST API!</p>"
    SPApiProxy.add_campaign(from_email='jane.roe@domain.com',
                            from_name='Jane Roe',
                            subject='Test campaign from REST API',
                            body=task_body,
                            addressbook_id=ADDRESSBOOK_ID,
                            campaign_name='Test campaign from REST API',
                            attachments={'attach1.txt': '12345\n', 'attach2.txt': '54321\n'})

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
