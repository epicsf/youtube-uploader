#!/usr/bin/python
import http.client
import httplib2
import os
import random
import time

import oauth2client
from apiclient.discovery import build
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = './client_secret.json'

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_refresh_token():
	try:
		with open('./refresh_token.txt') as f:
			for l in f:
				return l
	except FileNotFoundError:
		return None

def set_refresh_token(token):
	try:
		with open('./refresh_token.txt', 'w') as f:
			f.write(token)
	except FileNotFoundError:
		return None

def get_api_token():
	try:
		with open('./api_token.txt') as f:
			for l in f:
				return l
	except FileNotFoundError:
		return None

def set_api_token(token):
	try:
		with open('./api_token.txt', 'w') as f:
			f.write(token)
	except FileNotFoundError:
		return None

# Authorize the request and store authorization credentials.
def get_authenticated_service():
	flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
	refresh_token = get_refresh_token()
	if refresh_token:
		credentials = oauth2client.client.GoogleCredentials(
			None,
			flow.client_config['client_id'],
			flow.client_config['client_secret'],
      refresh_token,
      None,
      'https://accounts.google.com/o/oauth2/token',
      None,
    )
		http = credentials.authorize(httplib2.Http())
		credentials.refresh(http)
		set_refresh_token(credentials.refresh_token)
	else:
		credentials = flow.run_console()
		set_refresh_token(credentials.refresh_token)
	return build(
		API_SERVICE_NAME,
		API_VERSION,
		credentials=credentials,
	)
