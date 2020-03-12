# -*-coding:utf8-*-

""" SendPulse REST API usage example

Documentation:
    https://login.sendpulse.com/manual/rest-api/
    https://sendpulse.com/api
"""

from pysendpulse.pysendpulse import PySendPulse

if __name__ == "__main__":
    REST_API_ID = ''
    REST_API_SECRET = ''
    TOKEN_STORAGE = 'memcached'
    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)

    # Get list of tasks
    SPApiProxy.push_get_tasks()

    # Get list of websites
    SPApiProxy.push_get_websites()

    # Get amount of websites
    SPApiProxy.push_count_websites()

    # Get list of variables for website
    SPApiProxy.push_get_variables(WEBSITE_ID)

    # Get list of subscriptions for website
    SPApiProxy.push_get_subscriptions(WEBSITE_ID)

    # Get amount of subscriptions for website
    SPApiProxy.push_count_subscriptions(WEBSITE_ID)

    # Activate/Deactivate subscriber, state=1 - activate, state=2 - deactivate
    SPApiProxy.push_set_subscription_state(SUBSCRIBER_ID, STATE)

    # Create new push task
    SPApiProxy.push_create('Hello!', WEBSITE_ID, 'This is my first push message', '10', {'filter_lang':'en', 'filter': '{"variable_name":"some","operator":"or","conditions":[{"condition":"likewith","value":"a"},{"condition":"notequal","value":"b"}]}'})

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

    # Get a list of variables available on a mailing list
    SPApiProxy.get_addressbook_variables(ADDRESSBOOK_ID)

    # Changing a variable for an email contact
    SPApiProxy.set_variables_for_email(ADDRESSBOOK_ID, 'example@email.com', [{'name': 'foo', 'value': 'bar'}])

    # Get campaigns statistic for list of emails
    emails_list = ['test@test.com']
    SPApiProxy.get_emails_stat_by_campaigns(emails_list)

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

    # ****************  SMS ***************

    # Add phones to address book
    phones_for_add = [
        '11111111111',
        '22222222222'
    ]
    SPApiProxy.sms_add_phones(ADDRESSBOOK_ID, phones_for_add)

    # Add phones to address book
    phones_for_add = {
        "11111111111":
             [
                [
                      {"name" : "test1", "type" : "date", "value" : "2018-10-10 23:00:00"},
                      {"name" : "test2", "type" : "string", "value" : "asdasd"},
                      {"name" : "test3", "type" : "number", "value" : "123"}
                ]
             ],
        "22222222222":
                 [
                    [
                          {"name" : "test1", "type" : "date", "value" : "2018-10-10 23:00:00"},
                          {"name" : "test2", "type" : "string", "value" : "czxczx"},
                          {"name" : "test3", "type" : "number", "value" : "456"}
                    ]
                 ]
        }

    SPApiProxy.sms_add_phones_with_variables(ADDRESSBOOK_ID, phones_for_add)

    # Update phones variables from the address book
    phones_for_update = [
        '11111111111'
    ]
    variables = [
        {
            "name":"name","type":"string", "value":"Michael"
        }
    ]
    SPApiProxy.sms_update_phones_variables(ADDRESSBOOK_ID, phones_for_update, variables)

    # Get information about phone from the address book
    SPApiProxy.sms_get_phone_info(ADDRESSBOOK_ID, '1111111111')

    # Remove phones to address book
    phones_for_remove = [
        '11111111111',
        '22222222222'
    ]
    SPApiProxy.sms_delete_phones(ADDRESSBOOK_ID, phones_for_remove)

    # Get phones from the blacklist
    SPApiProxy.sms_get_blacklist()

    # Add phones to blacklist
    phones_for_add_to_blacklist = [
        '111222227',
        '222333337'
    ]
    SPApiProxy.sms_add_phones_to_blacklist(phones_for_add_to_blacklist, 'test')

    # Remove phones from blacklist
    phones_for_remove = [
        '11111111111',
        '22222222222'
    ]
    SPApiProxy.sms_delete_phones_from_blacklist(phones_for_remove)

    # Get info by phones from the blacklist
    phones = [
        '11111111111',
        '22222222222'
    ]
    SPApiProxy.sms_get_phones_info_from_blacklist(phones)

    # Create new sms campaign
    SPApiProxy.sms_add_campaign(SENDER_NAME, ADDRESSBOOK_ID, 'test')

    # Send sms by some phones
    phones_for_send = [
        '11111111111'
    ]
    SPApiProxy.sms_send(SENDER_NAME, phones_for_send, 'test')

    # Get list of sms campaigns
    date_from = '2018-04-10 23:00:00'
    date_to = '2018-05-10 23:00:00'
    SPApiProxy.sms_get_list_campaigns(date_from, date_to)

    # Get information about sms campaign
    SPApiProxy.sms_get_campaign_info(CAMPAIGN_ID)

    # Cancel sms campaign
    SPApiProxy.sms_cancel_campaign(CAMPAIGN_ID)

    # Get cost sms campaign
    SPApiProxy.sms_get_campaign_cost('sender', 'test', ADDRESSBOOK_ID)
    #SPApiProxy.sms_get_campaign_cost('sender', 'test', None, ['111111111'])

    # Remove sms campaign
    SPApiProxy.sms_delete_campaign(CAMPAIGN_ID)
