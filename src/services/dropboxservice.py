#!/usr/bin/env python

from dropbox.client import DropboxOAuth2FlowNoRedirect, DropboxClient
from dropbox import rest as dbrest

import utils
import constants

class DropboxService():

    @property
    def DESCRIPTION():
        return "dropbox"

    def __init__(self):
        self.__init()

    """
    initializes the service state for use.
    If necessary starts a setup process to obtain the necessary information
    to execute the operations (e.g. service access)
    """
    def __init(self):
        self.__request_client_token()
        return ""

    def __request_client_token(self):
        access_token = None
        req_flow = DropboxOAuth2FlowNoRedirect(constants.APP_KEY, constants.APP_SECRET)
        authorize_url = req_flow.start()
        print ("1. Go to: " + authorize_url)
        print ("2. Click \"Allow\" (you might have to log in first).")
        print ("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ").strip()

        ## TODO function that use this, should be the one to caugh the exception
        try:
            access_token, user_id = req_flow.finish(auth_code)
        except dbrest.ErrorResponse as e:
            print('Error: %s' % (e,))

        return access_token

    def backup(self):
        # Read from confi file the dirs or files
        # invoke the __backup function to actually perform the backup
        pass

    """
    Backups the list of files given by <files>
    if an entry of a file is a directory then all files in that directory will be backup up
    if it is a file only that file will be backed up
    """
    def __backup(self, files, dropbox_folder=None):
        ## TODO support for file filters
        ## TODO support for recursive folder iteration
        pass
