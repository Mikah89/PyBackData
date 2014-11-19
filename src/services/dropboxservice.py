#!/usr/bin/env python

from dropbox.client import DropboxOAuth2FlowNoRedirect, DropboxClient
from dropbox import rest as dbrest

import utils
import constants

class DropboxService():

    self.token = None
    self.dropbox_instance = None

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
        self.__check_configuration()

    def __check_configuration(self):
        if utils.get_config_section(DESCRIPTION.fget(), constants.AUTH_TOKEN) != None:
            return

        access_token = None
        req_flow = DropboxOAuth2FlowNoRedirect(constants.APP_KEY, constants.APP_SECRET)
        authorize_url = req_flow.start()
        print ("1. Go to: " + authorize_url)
        print ("2. Click \"Allow\" (you might have to log in first).")
        print ("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ").strip()

        ## TODO function that uses this, should be the one to caugh the exception
        try:
            access_token, user_id = req_flow.finish(auth_code)
        except dbrest.ErrorResponse as e:
            print('Error: %s' % (e,))

        utils.write_config_section(DESCRIPTION.fget(), constants.AUTH_TOKEN, access_token)
        self.token = acess_token
        self.dropbox_instance = DropboxClient(self.token)

        if not __has_backup_data():
            print ("You do not seem to have the backup file/folders configured. Pybackdata won't backup anything " + \
                   "without that setting.")
        if not __has_backup_folder():
            print ("You do not seem to have a target location  for the backups. Pybackdata won't backup anything " + \
                   "without that setting.")

    def backup(self):
        if not __has_backup_data():
            print ("No data to backup. Terminated!")
            return
        if not __has_backup_folder():
            print ("No destination location for backups. Terminated!")
            return

        file_list = self.__get_backup_data()
        self.__backup(file_list, constants.BACKUP_FOLDER)

    def __has_backup_data(self):
        return utils.get_config_section(DESCRIPTION.fget(), constants.BACKUP_DATA) != None

    def __has_backup_folder(self):
        return utils.get_config_section(DESCRIPTION.fget(), constants.BACKUP_FOLDER) != None

    ## The path for each file should be separated by a ;
    def __get_backup_data(self):
        raw_list = utils.get_config_section(DESCRIPTION.fget(), constants.BACKUP_DATA)
        split_list = raw_list.split(";")
        for idx in range(len(split_list)):
            split_list[idx] = split_list[idx].strip()

        return split_list

    """
    Backups the list of files given by <files>
    if an entry of a file is a directory then all files in that directory will be backup up
    if it is a file only that file will be backed up
    """
    def __backup(self, files, dropbox_folder=None):
        # for data in files:
        #     with open(data, 'rb') as datafile:
        #         self.dropbox_instance
        pass
