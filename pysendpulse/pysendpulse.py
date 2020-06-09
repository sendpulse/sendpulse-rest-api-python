# -*- encoding:utf8 -*-

""" API wrapper for interacting with SendPulse REST API
Documentation:
    https://login.sendpulse.com/manual/rest-api/
    https://sendpulse.com/api
"""

import os
import memcache
import requests
import logging
import base64
from hashlib import md5

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

class PySendPulse:
    """ SendPulse REST API python wrapper
    """
    __api_url = "https://api.sendpulse.com"
    __user_id = None
    __secret = None
    __token = None
    __token_file_path = ""
    __token_hash_name = None
    __storage_type = "FILE"
    __refresh_token = 0

    MEMCACHED_VALUE_TIMEOUT = 3600
    ALLOWED_STORAGE_TYPES = ['FILE', 'MEMCACHED']

    def __init__(self, user_id, secret, storage_type="FILE"):
        """ SendPulse API constructor

        @param user_id: string REST API ID from SendPulse settings
        @param secret: string REST API Secret from SendPulse settings
        @param storage_type: string FILE|MEMCACHED
        @raise: Exception empty credentials or get token failed
        """
        logger.info("Initialization SendPulse REST API Class")
        if not user_id or not secret:
            raise Exception("Empty ID or SECRET")

        self.__user_id = user_id
        self.__secret = secret
        self.__storage_type = storage_type.upper()
        m = md5()
        m.update("{}::{}".format(user_id, secret).encode('utf-8'))
        self.__token_hash_name = m.hexdigest()
        if self.__storage_type not in self.ALLOWED_STORAGE_TYPES:
            logger.warning("Wrong storage type '{}'. Allowed storage types are: {}".format(storage_type, self.ALLOWED_STORAGE_TYPES))
            logger.warning("Try to use 'FILE' instead.")
            self.__storage_type = 'FILE'
        logger.debug("Try to get security token from '{}'".format(self.__storage_type, ))
        if self.__storage_type == "MEMCACHED":
            mc = memcache.Client(['127.0.0.1:11211'])
            self.__token = mc.get(self.__token_hash_name)
        else:  # file
            filepath = "{}{}".format(self.__token_file_path, self.__token_hash_name)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    self.__token = f.readline()

            else:
                logger.error("Can't find file '{}' to read security token.".format(filepath))
        logger.debug("Got: '{}'".format(self.__token, ))
        if not self.__token and not self.__get_token():
            raise Exception("Could not connect to API. Please, check your ID and SECRET")

    def __get_token(self):
        """ Get new token from API server and store it in storage
        @return: boolean
        """
        logger.debug("Try to get new token from server")
        self.__refresh_token += 1
        data = {
            "grant_type": "client_credentials",
            "client_id": self.__user_id,
            "client_secret": self.__secret,
        }
        response = self.__send_request("oauth/access_token", "POST", data, False)
        if response.status_code != 200:
            return False
        self.__refresh_token = 0
        self.__token = response.json()['access_token']
        logger.debug("Got: '{}'".format(self.__token, ))
        if self.__storage_type == "MEMCACHED":
            logger.debug("Try to set token '{}' into 'MEMCACHED'".format(self.__token, ))
            mc = memcache.Client(['127.0.0.1:11211'])
            mc.set(self.__token_hash_name, self.__token, self.MEMCACHED_VALUE_TIMEOUT)
        else:
            filepath = "{}{}".format(self.__token_file_path, self.__token_hash_name)
            try:
                with open(filepath, 'w') as f:
                    f.write(self.__token)
                    logger.debug("Set token '{}' into 'FILE' '{}'".format(self.__token, filepath))
            except IOError:
                logger.warning("Can't create 'FILE' to store security token. Please, check your settings.")
        if self.__token:
            return True
        return False

    def __send_request(self, path, method="GET", params=None, use_token=True, use_json_content_type=False):
        """ Form and send request to API service

        @param path: sring what API url need to call
        @param method: HTTP method GET|POST|PUT|DELETE
        @param params: dict argument need to send to server
        @param use_token: boolean need to use token or not
        @param use_json_content_type: boolean need to convert params data to json or not
        @return: HTTP requests library object http://www.python-requests.org/
        """
        url = "{}/{}".format(self.__api_url, path)
        method.upper()
        logger.debug("__send_request method: {} url: '{}' with parameters: {}".format(method, url, params))
        if type(params) not in (dict, list):
            params = {}
        if use_token and self.__token:
            headers = {'Authorization': 'Bearer {}'.format(self.__token)}
        else:
            headers = {}
        if use_json_content_type and params:
            headers['Content-Type'] = 'application/json'
            params = json.dumps(params)

        if method == "POST":
            response = requests.post(url, headers=headers, data=params)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=params)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, data=params)
        else:
            response = requests.get(url, headers=headers, params=params)
        if response.status_code == 401 and self.__refresh_token == 0:
            self.__get_token()
            return self.__send_request(path, method, params)
        elif response.status_code == 404:
            logger.warning("404: Sorry, the page you are looking for could not be found.")
            logger.debug("Raw_server_response: {}".format(response.text, ))
        elif response.status_code == 500:
            logger.critical("Whoops, looks like something went wrong on the server. Please contact with out support tech@sendpulse.com.")
        else:
            try:
                logger.debug("Request response: {}".format(response.json(), ))
            except:
                logger.critical("Raw server response: {}".format(response.text, ))
                return response.status_code
        return response

    def __handle_result(self, data):
        """ Process request results

        @param data:
        @return: dictionary with response message and/or http code
        """
        if 'status_code' not in data:
            if data.status_code == 200:
                logger.debug("Hanle result: {}".format(data.json(), ))
                return data.json()
            elif data.status_code == 404:
                response = {
                    'is_error': True,
                    'http_code': data.status_code,
                    'message': "Sorry, the page you are looking for {} could not be found.".format(data.url, )
                }
            elif data.status_code == 500:
                response = {
                    'is_error': True,
                    'http_code': data.status_code,
                    'message': "Whoops, looks like something went wrong on the server. Please contact with out support tech@sendpulse.com."
                }
            else:
                response = {
                    'is_error': True,
                    'http_code': data.status_code
                }
                response.update(data.json())
        else:
            response = {
                'is_error': True,
                'http_code': data
            }
        logger.debug("Hanle result: {}".format(response, ))
        return {'data': response}

    def __handle_error(self, custom_message=None):
        """ Process request errors

        @param custom_message:
        @return: dictionary with response custom error message and/or error code
        """
        message = {'is_error': True}
        if custom_message is not None:
            message['message'] = custom_message
        logger.error("Hanle error: {}".format(message, ))
        return message

    # ------------------------------------------------------------------ #
    #                             BALANCE                                #
    # ------------------------------------------------------------------ #

    def get_balance(self, currency=None):
        """ Get balance

        @param currency: USD, EUR, GBP, UAH, RUR, INR, JPY
        @return: dictionary with response message
        """
        logger.info("Function call: get_balance")
        return self.__handle_result(self.__send_request('balance/{}'.format(currency.upper() if currency else ''), ))

    # ------------------------------------------------------------------ #
    #                           ADDRESSBOOKS                             #
    # ------------------------------------------------------------------ #

    def add_addressbook(self, addressbook_name):
        """ Create addressbook

        @param addressbook_name: string name for addressbook
        @return: dictionary with response message
        """
        logger.info("Function call: create_addressbook: '{}'".format(addressbook_name, ))
        return self.__handle_error("Empty AddressBook name") if not addressbook_name else self.__handle_result(self.__send_request('addressbooks', 'POST', {'bookName': addressbook_name}))

    def edit_addressbook(self, id, new_addressbook_name):
        """ Edit addressbook name

        @param id: unsigned int addressbook ID
        @param new_addressbook_name: string new name for addressbook
        @return: dictionary with response message
        """
        logger.info("Function call: edit_addressbook: '{}' with new addressbook name '{}'".format(id, new_addressbook_name))
        if not id or not new_addressbook_name:
            return self.__handle_error("Empty new name or addressbook id")
        return self.__handle_result(self.__send_request('addressbooks/{}'.format(id), 'PUT', {'name': new_addressbook_name}))

    def delete_addressbook(self, id):
        """ Remove addressbook

        @param id: unsigned int addressbook ID
        @return: dictionary with response message
        """
        logger.info("Function call: remove_addressbook: '{}'".format(id, ))
        return self.__handle_error("Empty addressbook id") if not id else self.__handle_result(self.__send_request('addressbooks/{}'.format(id), 'DELETE'))

    def get_list_of_addressbooks(self, limit=0, offset=0):
        """ Get list of addressbooks

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @return: dictionary with response message
        """
        logger.info("Function call: get_list_of_addressbooks")
        return self.__handle_result(self.__send_request('addressbooks', 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def get_addressbook_info(self, id):
        """ Get information about addressbook

        @param id: unsigned int addressbook ID
        @return: dictionary with response message
        """
        logger.info("Function call: get_addressbook_info: '{}'".format(id, ))
        return self.__handle_error("Empty addressbook id") if not id else self.__handle_result(self.__send_request('addressbooks/{}'.format(id)))

    def get_addressbook_variables(self, id):
        """ Get a list of variables available on a mailing list

        @param id: unsigned int addressbook ID
        @return: list with variables of addressbook
        """
        logger.info("Function call: get_addressbook_variables_list: '{}'".format(id, ))
        return self.__handle_error("Empty addressbook id") if not id else self.__handle_result(self.__send_request('addressbooks/{}/variables'.format(id)))

    # ------------------------------------------------------------------ #
    #                        EMAIL  ADDRESSES                            #
    # ------------------------------------------------------------------ #

    def get_emails_from_addressbook(self, id, limit=0, offset=0):
        """ List email addresses from addressbook

        @param id: unsigned int addressbook ID
        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @return: dictionary with response message
        """
        logger.info("Function call: get_emails_from_addressbook: '{}'".format(id, ))
        return self.__handle_error("Empty addressbook id") if not id else self.__handle_result(self.__send_request('addressbooks/{}/emails'.format(id), 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def add_emails_to_addressbook(self, id, emails):
        """ Add new emails to addressbook

        @param id: unsigned int addressbook ID
        @param emails: list of dictionaries [
                {'email': 'test@test.com', 'variables': {'varname_1': 'value_1', ..., 'varname_n': 'value_n' }},
                {...},
                {'email': 'testn@testn.com'}}
            ]
        @return: dictionary with response message
        """
        logger.info("Function call: add_emails_to_addressbook into: {}".format(id, ))
        if not id or not emails:
            self.__handle_error("Empty addressbook id or emails")
        try:
            emails = json.dumps(emails)
        except:
            logger.debug("Emails: {}".format(emails))
            return self.__handle_error("Emails list can't be converted by JSON library")
        return self.__handle_result(self.__send_request('addressbooks/{}/emails'.format(id), 'POST', {'emails': emails}))

    def delete_emails_from_addressbook(self, id, emails):
        """ Delete email addresses from addressbook

        @param id: unsigned int addressbook ID
        @param emails: list of emails ['test_1@test_1.com', ..., 'test_n@test_n.com']
        @return: dictionary with response message
        """
        logger.info("Function call: delete_emails_from_addressbook from: {}".format(id, ))
        if not id or not emails:
            self.__handle_error("Empty addressbook id or emails")
        try:
            emails = json.dumps(emails)
        except:
            logger.debug("Emails: {}".format(emails))
            return self.__handle_error("Emails list can't be converted by JSON library")
        return self.__handle_result(self.__send_request('addressbooks/{}/emails'.format(id), 'DELETE', {'emails': emails}))

    def get_emails_stat_by_campaigns(self, emails):
        """ Get campaigns statistic for list of emails

        @param emails: list of emails ['test_1@test_1.com', ..., 'test_n@test_n.com']
        @return: dictionary with response message
        """
        logger.info("Function call: get_emails_stat_by_campaigns")
        if not emails:
            self.__handle_error("Empty emails")
        try:
            emails = json.dumps(emails)
        except:
            logger.debug("Emails: {}".format(emails))
            return self.__handle_error("Emails list can't be converted by JSON library")
        return self.__handle_result(self.__send_request('emails/campaigns', 'POST', {'emails': emails}))

    def set_variables_for_email(self, id, email, variables):
        """ Set variables for email

        @param id: unsigned int addressbook ID
        @param email: string 
        @param variables: dictionary
        @return: dictionary with response message
        """
        logger.info("Function call: set_variables_for_email: '{}' with email: '{}' new variables: '{}'".format(id, email, variables))
        return self.__handle_error("Empty addressbook id") if not id else self.__handle_result(self.__send_request('addressbooks/{}/emails/variable'.format(id), 'POST', {'email': email, 'variables': variables}, True, True))

    # ------------------------------------------------------------------ #
    #                        EMAIL  CAMPAIGNS                            #
    # ------------------------------------------------------------------ #

    def get_campaign_cost(self, id):
        """ Get cost of campaign based on addressbook

        @param id: unsigned int addressbook ID
        @return: dictionary with response message
        """
        logger.info("Function call: get_campaign_cost: '{}'".format(id, ))
        return self.__handle_error("Empty addressbook id") if not id else self.__handle_result(self.__send_request('addressbooks/{}/cost'.format(id)))

    def get_list_of_campaigns(self, limit=0, offset=0):
        """ Get list of campaigns

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @return: dictionary with response message
        """
        logger.info("Function call: get_list_of_campaigns")
        return self.__handle_result(self.__send_request('campaigns', 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def get_campaign_info(self, id):
        """ Get information about campaign

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        logger.info("Function call: get_campaign_info from: {}".format(id, ))
        return self.__handle_error("Empty campaign id") if not id else self.__handle_result(self.__send_request('campaigns/{}'.format(id, )))

    def get_campaign_stat_by_countries(self, id):
        """ Get information about campaign

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        logger.info("Function call: get_campaign_stat_by_countries from: '{}'".format(id, ))
        return self.__handle_error("Empty campaign id") if not id else self.__handle_result(self.__send_request('campaigns/{}/countries'.format(id, )))

    def get_campaign_stat_by_referrals(self, id):
        """ Get campaign statistic by referrals

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        logger.info("Function call: get_campaign_stat_by_referrals from: '{}'".format(id, ))
        return self.__handle_error("Empty campaign id") if not id else self.__handle_result(self.__send_request('campaigns/{}/referrals'.format(id, )))

    def add_campaign(self, from_email, from_name, subject, body, addressbook_id, campaign_name='', attachments=None):
        """ Create new campaign

        @param from_email: string senders email
        @param from_name: string senders name
        @param subject: string campaign title
        @param body: string campaign body
        @param addressbook_id: unsigned int addressbook ID
        @param campaign_name: string campaign name
        @param attachments: dictionary with {filename_1: filebody_1, ..., filename_n: filebody_n}
        @return: dictionary with response message
        """
        if not attachments:
            attachments = {}
        logger.info("Function call: create_campaign")
        if not from_name or not from_email:
            return self.__handle_error('Seems you pass not all data for sender: Email or Name')
        elif not subject or not body:
            return self.__handle_error('Seems you pass not all data for task: Title or Body')
        elif not addressbook_id:
            return self.__handle_error('Seems you not pass addressbook ID')
        if not attachments:
            attachments = {}
        return self.__handle_result(self.__send_request('campaigns', 'POST', {
            'sender_name': from_name,
            'sender_email': from_email,
            'subject': subject,
            'body': base64.b64encode(body),
            'list_id': addressbook_id,
            'name': campaign_name,
            'attachments': json.dumps(attachments)
        }))

    def cancel_campaign(self, id):
        """ Cancel campaign

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        logger.info("Function call: cancel_campaign : '{}'".format(id, ))
        return self.__handle_error("Empty campaign id") if not id else self.__handle_result(self.__send_request('campaigns/{}'.format(id, ), 'DELETE'))

    # ------------------------------------------------------------------ #
    #                        EMAIL  SENDERS                              #
    # ------------------------------------------------------------------ #

    def get_list_of_senders(self):
        """ List of all senders

        @return: dictionary with response message
        """
        logger.info("Function call: get_senders")
        return self.__handle_result(self.__send_request('senders'))

    def add_sender(self, email, name):
        """ Add sender
        @param email: string sender from email
        @param name: string senders from name
        @return: dictionary with response message
        """
        logger.info("Function call: add_sender: '{}' '{}'".format(email, name))
        if not name or not email:
            return self.__handle_error("Seems you passing not all data for sender: Email: '{}' or Name: '{}'".format(email, name))
        return self.__handle_result(self.__send_request('senders', 'POST', {'email': email, 'name': name}))

    def delete_sender(self, email):
        """ Delete sender
        @param email: string sender from email
        @return: dictionary with response message
        """
        logger.info("Function call: delete_sender: '{}'".format(email, ))
        return self.__handle_error('Empty sender email') if not email else self.__handle_result(self.__send_request('senders', 'DELETE', {'email': email}))

    def activate_sender(self, email, code):
        """ Activate new sender
        @param email: string sender from email
        @param code: string activation code
        @return: dictionary with response message
        """
        logger.info("Function call: activate_sender '{}' with code '{}'".format(email, code))
        if not email or not code:
            return self.__handle_error("Empty email '{}' or activation code '{}'".format(email, code))
        return self.__handle_result(self.__send_request('senders/{}/code'.format(email, ), 'POST', {'code': code}))

    def send_sender_activation_email(self, email):
        """ Request email with activation code

        @param email: string sender from email
        @return: dictionary with response message
        """
        logger.info("Function call: send_sender_activation_email for '{}'".format(email, ))
        return self.__handle_error('Empty sender email') if not email else self.__handle_result(self.__send_request('senders/{}/code'.format(email, )))

    # ------------------------------------------------------------------ #
    #                              EMAILS                                #
    # ------------------------------------------------------------------ #

    def get_email_info_from_one_addressbooks(self, id, email):
        """ Get information about email address from one addressbook

        @param id: unsigned int addressbook ID
        @param email: string valid email address
        @return: dictionary with response message
        """
        logger.info("Function call: get_email_info_from_one_addressbooks from: '{}'".format(id, ))
        if not id or not email:
            self.__handle_error("Empty addressbook id or email")
        return self.__handle_result(self.__send_request('addressbooks/{}/emails/{}'.format(id, email)))

    def get_email_info_from_all_addressbooks(self, email):
        """ Get global information about email

        @param email: string email
        @return: dictionary with response message
        """
        logger.info("Function call: get_email_info_from_all_addressbooks for '{}'".format(email, ))
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('emails/{}'.format(email, )))

    def delete_email_from_all_addressooks(self, email):
        """ Remove email from all addressbooks

        @param email: string email
        @return: dictionary with response message
        """
        logger.info("Function call: delete_email_from_all_addressooks for '{}'".format(email, ))
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('emails/{}'.format(email, ), 'DELETE'))

    def get_email_statistic_by_campaigns(self, email):
        """ Get email statistic by all campaigns

        @param email: string email
        @return: dictionary with response message
        """
        logger.info("Function call: get_email_statistic_by_campaigns for '{}'".format(email, ))
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('emails/{}/campaigns'.format(email, )))

    def get_emails_in_blacklist(self, limit=0, offset=0):
        """ Get all emails from blacklist

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @return: dictionary with response message
        """
        logger.info("Function call: get_emails_in_blacklist")
        return self.__handle_result(self.__send_request('blacklist', 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def add_email_to_blacklist(self, email, comment=''):
        """ Add email to blacklist

        @param email: string emails divided by commas 'email_1, ..., email_n'
        @param comment: string describing why email added to blacklist
        @return: dictionary with response message
        """
        logger.info("Function call: add_email_to_blacklist for '{}'".format(email, ))
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('blacklist', 'POST', {'emails': base64.b64encode(email), 'comment': comment}))

    def delete_email_from_blacklist(self, email):
        """ Remove emails from blacklist

        @param email: string email
        @return: dictionary with response message
        """
        logger.info("Function call: delete_email_from_blacklist for '{}'".format(email, ))
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('blacklist', 'DELETE', {'emails': base64.b64encode(email)}))

    # ------------------------------------------------------------------ #
    #                              SMTP                                  #
    # ------------------------------------------------------------------ #

    def smtp_get_list_of_emails(self, limit=0, offset=0, date_from=None, date_to=None, sender=None, recipient=None):
        """ SMTP: get list of emails

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @param date_from: string date for filter in 'YYYY-MM-DD'
        @param date_to: string date for filter in 'YYYY-MM-DD'
        @param sender:  string from email
        @param recipient: string for email
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_get_list_of_emails")
        return self.__handle_result(self.__send_request('smtp/emails', 'GET', {
            'limit': limit,
            'offset': offset,
            'from': date_from,
            'to': date_to,
            'sender': sender,
            'recipient': recipient
        }))

    def smtp_get_email_info_by_id(self, id):
        """ Get information about email by ID

        @param id: unsigned int email id
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_get_email_info_by_id for '{}'".format(id, ))
        return self.__handle_error('Empty email') if not id else self.__handle_result(self.__send_request('smtp/emails/{}'.format(id, )))

    def smtp_add_emails_to_unsubscribe(self, emails):
        """ SMTP: add emails to unsubscribe list

        @param emails: list of dictionaries [{'email': 'test_1@test_1.com', 'comment': 'comment_1'}, ..., {'email': 'test_n@test_n.com', 'comment': 'comment_n'}]
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_add_emails_to_unsubscribe")
        return self.__handle_error('Empty email') if not emails else self.__handle_result(self.__send_request('smtp/unsubscribe', 'POST', {'emails': json.dumps(emails)}))

    def smtp_delete_emails_from_unsubscribe(self, emails):
        """ SMTP: remove emails from unsubscribe list

        @param emails: list of dictionaries ['test_1@test_1.com', ..., 'test_n@test_n.com']
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_delete_emails_from_unsubscribe")
        return self.__handle_error('Empty email') if not emails else self.__handle_result(self.__send_request('smtp/unsubscribe', 'DELETE', {'emails': json.dumps(emails)}))

    def smtp_get_list_of_ip(self):
        """ SMTP: get list of IP

        @return: dictionary with response message
        """
        logger.info("Function call: smtp_get_list_of_ip")
        return self.__handle_result(self.__send_request('smtp/ips'))

    def smtp_get_list_of_allowed_domains(self):
        """ SMTP: get list of allowed domains

        @return: dictionary with response message
        """
        logger.info("Function call: smtp_get_list_of_allowed_domains")
        return self.__handle_result(self.__send_request('smtp/domains'))

    def smtp_add_domain(self, email):
        """ SMTP: add and verify new domain

        @param email: string valid email address on the domain you want to verify. We will send an email message to the specified email address with a verification link.
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_add_domain")
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('smtp/domains', 'POST', {'email': email}))

    def smtp_verify_domain(self, email):
        """ SMTP: verify domain already added domain

        @param email: string valid email address on the domain you want to verify. We will send an email message to the specified email address with a verification link.
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_verify_domain")
        return self.__handle_error('Empty email') if not email else self.__handle_result(self.__send_request('smtp/domains/{}'.format(email, )))

    def smtp_send_mail(self, email):
        """ SMTP: send email

        @param email: string valid email address. We will send an email message to the specified email address with a verification link.
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_send_mail")
        if (not email.get('html') or not email.get('text')) and not email.get('template'):
            return self.__handle_error('Seems we have empty body')
        elif not email.get('subject'):
            return self.__handle_error('Seems we have empty subject')
        elif not email.get('from') or not email.get('to'):
            return self.__handle_error("Seems we have empty some credentials 'from': '{}' or 'to': '{}' fields".format(email.get('from'), email.get('to')))
        email['html'] = base64.b64encode(email.get('html').encode('utf-8')).decode('utf-8') if email['html'] else None
        return self.__handle_result(self.__send_request('smtp/emails', 'POST', {'email': json.dumps(email)}))

    def smtp_send_mail_with_template(self, email):
        """ SMTP: send email with custom template

        @param email: string valid email address. We will send an email message to the specified email address with a verification link.
        @return: dictionary with response message
        """
        logger.info("Function call: smtp_send_mail_with_template")
        if not email.get('template'):
            return self.__handle_error('Seems we have empty template')
        elif not email.get('template').get('id'):
            return self.__handle_error('Seems we have empty template id')
        email['html'] = email['text'] = None
        return self.smtp_send_mail(email)

    # ------------------------------------------------------------------ #
    #                              PUSH                                  #
    # ------------------------------------------------------------------ #

    def push_get_tasks(self, limit=0, offset=0):
        """ PUSH: get list of tasks

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @return: dictionary with response message
        """
        logger.info("Function call: push_get_tasks")
        return self.__handle_result(self.__send_request('push/tasks', 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def push_get_websites(self, limit=0, offset=0):
        """ PUSH: get list of websites

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @return: dictionary with response message
        """
        logger.info("Function call: push_get_websites")
        return self.__handle_result(self.__send_request('push/websites', 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def push_count_websites(self):
        """ PUSH: get amount of websites

        @return: dictionary with response message
        """
        logger.info("Function call: push_count_websites")
        return self.__handle_result(self.__send_request('push/websites/total', 'GET', {}))

    def push_get_variables(self, id):
        """ PUSH: get list of all variables for website

        @param id: unsigned int website id
        @return: dictionary with response message
        """
        logger.info("Function call: push_get_variables for {}".format(id))
        return self.__handle_result(self.__send_request('push/websites/{}/variables'.format(id), 'GET', {}))

    def push_get_subscriptions(self, id, limit=0, offset=0):
        """ PUSH: get list of all subscriptions for website

        @param limit: unsigned int max limit of records. The max value is 100
        @param offset: unsigned int how many records pass before selection
        @param id: unsigned int website id
        @return: dictionary with response message
        """
        logger.info("Function call: push_get_subscriptions for {}".format(id))
        return self.__handle_result(self.__send_request('push/websites/{}/subscriptions'.format(id), 'GET', {'limit': limit or 0, 'offset': offset or 0}))

    def push_count_subscriptions(self, id):
        """ PUSH: get amount of subscriptions for website

        @param id: unsigned int website id
        @return: dictionary with response message
        """
        logger.info("Function call: push_count_subscriptions for {}".format(id))
        return self.__handle_result(self.__send_request('push/websites/{}/subscriptions/total'.format(id), 'GET', {}))

    def push_set_subscription_state(self, subscription_id, state_value):
        """ PUSH: get amount of subscriptions for website

        @param subscription_id: unsigned int subscription id
        @param state_value: unsigned int state value. Can be 0 or 1
        @return: dictionary with response message
        """
        logger.info("Function call: push_set_subscription_state for {} to state {}".format(subscription_id, state_value))
        return self.__handle_result(self.__send_request('/push/subscriptions/state', 'POST', {'id': subscription_id, 'state': state_value}))

    def push_create(self, title, website_id, body, ttl, additional_params={}):
        """ PUSH: create new push

        @param title: string push title
        @param website_id: unsigned int website id
        @param body: string push body
        @param ttl: unsigned int ttl for push messages
        @param additional_params: dictionary additional params for push task
        @return: dictionary with response message
        """
        data_to_send = {
            'title': title,
            'website_id': website_id,
            'body': body,
            'ttl': ttl
        }
        if additional_params:
            data_to_send.update(additional_params)

        logger.info("Function call: push_create")
        return self.__handle_result(self.__send_request('/push/tasks', 'POST', data_to_send))

    # ------------------------------------------------------------------ #
    #                               SMS                                  #
    # ------------------------------------------------------------------ #

    def sms_add_phones(self, addressbook_id, phones):
        """ SMS: add phones from the address book

        @return: dictionary with response message
        """
        if not addressbook_id or not phones:
            return self.__handle_error("Empty addressbook id or phones")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'addressBookId': addressbook_id,
            'phones': phones
        }

        logger.info("Function call: sms_add_phones")
        return self.__handle_result(self.__send_request('sms/numbers', 'POST', data_to_send))

    def sms_add_phones_with_variables(self, addressbook_id, phones):
        """ SMS: add phones with variables from the address book

        @return: dictionary with response message
        """
        if not addressbook_id or not phones:
            return self.__handle_error("Empty addressbook id or phones")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'addressBookId': addressbook_id,
            'phones': phones
        }

        logger.info("Function call: sms_add_phones_with_variables")
        return self.__handle_result(self.__send_request('sms/numbers/variables', 'POST', data_to_send))

    def sms_delete_phones(self, addressbook_id, phones):
        """ SMS: remove phones from the address book

        @return: dictionary with response message
        """
        if not addressbook_id or not phones:
            return self.__handle_error("Empty addressbook id or phones")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'addressBookId': addressbook_id,
            'phones': phones
        }

        logger.info("Function call: sms_delete_phones")
        return self.__handle_result(self.__send_request('sms/numbers', 'DELETE', data_to_send))

    def sms_get_phone_info(self, addressbook_id, phone):
        """ SMS: Get information about phone from the address book

        @return: dictionary with response message
        """
        if not addressbook_id or not phone:
            return self.__handle_error("Empty addressbook id or phone")

        logger.info("Function call: sms_get_phone_info")
        return self.__handle_result(self.__send_request('sms/numbers/info/' + str(addressbook_id) + '/' + str(phone), 'GET'))

    def sms_update_phones_variables(self, addressbook_id, phones, variables):
        """ SMS: update phones variables from the address book

        @return: dictionary with response message
        """
        if not addressbook_id or not phones or not variables:
            return self.__handle_error("Empty addressbook id or phones or variables")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        try:
            variables = json.dumps(variables)
        except:
            logger.debug("Variables: {}".format(variables))
            return self.__handle_error("Variables list can't be converted by JSON library")

        data_to_send = {
            'addressBookId': addressbook_id,
            'phones': phones,
            'variables': variables
        }

        logger.info("Function call: sms_update_phones_variables")
        return self.__handle_result(self.__send_request('sms/numbers', 'PUT', data_to_send))

    def sms_get_blacklist(self):
        """ SMS: get phones from the blacklist

        @return: dictionary with response message
        """
        logger.info("Function call: sms_get_blacklist")
        return self.__handle_result(self.__send_request('sms/black_list', 'GET', {}))

    def sms_get_phones_info_from_blacklist(self, phones):
        """ SMS: get info by phones from the blacklist

        @param phones: array phones
        @return: dictionary with response message
        """
        if not phones:
            return self.__handle_error("Empty phones")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'phones': phones
        }

        logger.info("Function call: sms_add_phones_to_blacklist")
        return self.__handle_result(self.__send_request('sms/black_list/by_numbers', 'GET', data_to_send))

    def sms_add_phones_to_blacklist(self, phones, comment):
        """ SMS: add phones to blacklist

        @param phones: array phones
        @param comment: string describing why phones added to blacklist
        @return: dictionary with response message
        """
        if not phones:
            return self.__handle_error("Empty phones")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'phones': phones,
            'description': comment
        }

        logger.info("Function call: sms_add_phones_to_blacklist")
        return self.__handle_result(self.__send_request('sms/black_list', 'POST', data_to_send))

    def sms_delete_phones_from_blacklist(self, phones):
        """ SMS: remove phones from blacklist

        @param phones: array phones
        @return: dictionary with response message
        """
        if not phones:
            return self.__handle_error("Empty phones")
        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'phones': phones
        }

        logger.info("Function call: sms_add_phones_to_blacklist")
        return self.__handle_result(self.__send_request('sms/black_list', 'DELETE', data_to_send))

    def sms_add_campaign(self, sender_name, addressbook_id, body, date=None, transliterate=False):
        """ Create new sms campaign

        @param sender_name: string senders name
        @param addressbook_id: unsigned int addressbook ID
        @param body: string campaign body
        @param date: string date for filter in 'Y-m-d H:i:s'
        @param transliterate: boolean need to transliterate sms body or not
        @return: dictionary with response message
        """

        logger.info("Function call: sms_create_campaign")
        if not sender_name:
            return self.__handle_error('Seems you not pass sender name')
        if not addressbook_id:
            return self.__handle_error('Seems you not pass addressbook ID')
        if not body:
            return self.__handle_error('Seems you not pass sms text')

        data_to_send = {
            'sender': sender_name,
            'addressBookId': addressbook_id,
            'body': body,
            'date': date,
            'transliterate': transliterate,
        }

        return self.__handle_result(self.__send_request('sms/campaigns', 'POST', data_to_send))

    def sms_send(self, sender_name, phones, body, date=None, transliterate=False):
        """ Send sms by some phones

        @param sender_name: string senders name
        @param phones: array phones
        @param body: string campaign body
        @param date: string date for filter in 'Y-m-d H:i:s'
        @param transliterate: boolean need to transliterate sms body or not
        @return: dictionary with response message
        """

        logger.info("Function call: sms_send")
        if not sender_name:
            return self.__handle_error('Seems you not pass sender name')
        if not phones:
            return self.__handle_error("Empty phones")
        if not body:
            return self.__handle_error('Seems you not pass sms text')

        try:
            phones = json.dumps(phones)
        except:
            logger.debug("Phones: {}".format(phones))
            return self.__handle_error("Phones list can't be converted by JSON library")

        data_to_send = {
            'sender': sender_name,
            'phones': phones,
            'body': body,
            'date': date,
            'transliterate': transliterate,
        }

        return self.__handle_result(self.__send_request('sms/send', 'POST', data_to_send))

    def sms_get_list_campaigns(self, date_from, date_to):
        """ SMS: get list of campaigns

        @param date_from: string date for filter in 'Y-m-d H:i:s'
        @param date_to: string date for filter in 'Y-m-d H:i:s'
        @return: dictionary with response message
        """
        logger.info("Function call: sms_get_list_campaigns")

        data_to_send = {
            'dateFrom': date_from,
            'dateTo': date_to
        }
        return self.__handle_result(self.__send_request('sms/campaigns/list', 'GET', data_to_send))

    def sms_get_campaign_info(self, id):
        """ Get information about sms campaign

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        if not id:
            return self.__handle_error("Empty campaign id")

        logger.info("Function call: sms_get_campaign_info from: {}".format(id, ))
        return self.__handle_result(self.__send_request('/sms/campaigns/info/{}'.format(id, )))

    def sms_cancel_campaign(self, id):
        """ Cancel sms campaign

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        if not id:
            return self.__handle_error("Empty campaign id")

        logger.info("Function call: sms_cancel_campaign : '{}'".format(id, ))
        return self.__handle_result(self.__send_request('sms/campaigns/cancel/{}'.format(id, ), 'PUT'))

    def sms_get_campaign_cost(self, sender, body, addressbook_id=None, phones=None):
        """ Get cost sms campaign

        @param id: unsigned int campaign ID
        @return: dictionary with response message
        """
        if not sender:
            return self.__handle_error("Empty sender")
        if not body:
            return self.__handle_error("Empty sms body")
        if not addressbook_id and not phones:
            return self.__handle_error("Empty addressbook id or phones")

        data_to_send = {
            'sender': sender,
            'body': body,
            'addressBookId': addressbook_id
        }
        if phones:
            try:
                data_to_send.update({'phones': json.dumps(phones)})
            except:
                logger.debug("Phones: {}".format(phones))
                return self.__handle_error("Phones list can't be converted by JSON library")

        logger.info("Function call: sms_get_campaign_cost")
        return self.__handle_result(self.__send_request('sms/campaigns/cost', 'GET', data_to_send))

    def sms_delete_campaign(self, id):
        """ SMS: remove sms campaign

        @return: dictionary with response message
        """
        if not id:
            return self.__handle_error("Empty sms campaign id")

        data_to_send = {
            'id': id
        }

        logger.info("Function call: sms_delete_campaign")
        return self.__handle_result(self.__send_request('sms/campaigns', 'DELETE', data_to_send))
