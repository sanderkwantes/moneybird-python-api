#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rauth import OAuth2Service

print '\n\n##############################################################'
print '################## PYTHON MONEYBIRD OAUTH2 ###################'
print '##############################################################'

print(
    "\nBefore you can use OAuth2 in our API, you need to register\n"
    "your application with MoneyBird. Registration allows us to\n"
    "see which application is authenticating and who is the\n"
    "owner of the application. Registration is a one-time event\n"
    "and can be done by logging in to your MoneyBird account and\n"
    "visit the page:\n\n"

    "https://moneybird.com/user/applications/new.\n\n"

    "After registration you will receive a Client ID\n"
    "and Client Secret. You will use these tokens to identify\n"
    "your application when requesting access for users.\n"
)

print '##############################################################'
print '################## CLIENT ID & CLIENT SECRET #################'
print '##############################################################\n'

client_id = raw_input("Paste Client ID: ")
client_secret = raw_input("Paste Client Secret: ")

print '\n##############################################################'
print '################## CALLBACK/REDIRECT URL  ####################'
print '##############################################################\n'

redirect_uri = raw_input(
    "Enter Callback URL: [http://localhost/callback]:") or "http://localhost/callback"

print '\n##############################################################'
print '################## DEFINE ACCESS TO SCOPES ###################'
print '##############################################################\n'

moneybird = OAuth2Service(
    client_id=client_id,
    client_secret=client_secret,
    name='moneybird',
    authorize_url='https://moneybird.com/oauth/authorize',
    access_token_url='https://moneybird.com/oauth/token',
    base_url='https://moneybird.com')

sales_invoices = raw_input("Access to Sales Invoices?: Y/N [Y]:") or "Y"
documents = raw_input("Access to Documents?: Y/N [Y]:") or "Y"
estimates = raw_input("Access to Estimates?: Y/N [Y]:") or "Y"
bank = raw_input("Access to Bank?: Y/N [Y]:") or "Y"
settings = raw_input("Access to Settings?: Y/N [Y]:") or "Y"

if sales_invoices is "Y":
    sc_sal = 'sales_invoices '
else:
    sc_sal = ''

if documents is "Y":
    sc_doc = 'documents '
else:
    sc_doc = ''

if estimates is "Y":
    sc_est = 'estimates '
else:
    sc_est = ''

if bank is "Y":
    sc_ban = 'bank '
else:
    sc_ban = ''

if settings is "Y":
    sc_set = 'settings '
else:
    sc_set = ''

scopes = sc_sal + sc_doc + sc_est + sc_ban + sc_set

params = {'scope': scopes,
          'response_type': 'code',
          'redirect_uri': redirect_uri}

url = moneybird.get_authorize_url(**params)

print '\n##############################################################'
print '################## AUTHORIZE APPLICATION #####################'
print '##############################################################\n'

print 'Paste the following URL in your browser and authorize the request:\n\n' + url + '\n'

print '##############################################################'
print '################## COPY CODE FROM BROWSER ####################'
print '##############################################################\n'

print 'In your browser you will now find the code in the url after:\n'
print '%s?code=\n' % redirect_uri

print '##############################################################'
print '################## OBTAIN ACCESS TOKEN #######################'
print '##############################################################\n'

data = {'code': raw_input('Paste your code here: '),
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri}

response = moneybird.get_raw_access_token(data=data)
response = response.json()

print '\n##############################################################'
print '################## YOUR ACCESS TOKEN! ########################'
print '##############################################################\n'

print 'Your Access Token is:\n\n' + response.get('access_token') + '\n'

print '##############################################################'
print '################## GOOD LUCK! ################################'
print '##############################################################\n'
