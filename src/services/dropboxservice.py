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
        self.token = None
        self.dropbox_instance = None
        self.__init()

    """
    initializes the service state for use.
    If necessary starts a setup process to obtain the necessary information
    to execute the operations (e.g. service access)
    """
    def __init(self):
        self.__check_configuration()
        ## TODO what if it fails?
        self.dropbox_instance = DropboxClient(self.token)

    def __check_configuration(self):
        self.token = utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.AUTH_TOKEN)
        if self.token != None:
            ## TODO check if it is sstill valid... user may have unistalled the app
            return

        self.__fill_app_keys()

        access_token = None
        app_key = utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.APP_KEY)
        app_secret = utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.APP_SECRET)
        req_flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)
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

        utils.write_config_section(DropboxService.DESCRIPTION.fget(), constants.AUTH_TOKEN, access_token)
        self.token = access_token

        if not self.__has_backup_data():
            print ("You do not seem to have the backup file/folders configured. Pybackdata won't backup anything " + \
                   "without that setting.")
        if not self.__has_backup_folder():
            print ("You do not seem to have a target location  for the backups. Pybackdata won't backup anything " + \
                   "without that setting.")

    def __fill_app_keys(self):
        to_update = []
        if utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.APP_KEY) == None:
            app_key = input("Enter your development app key: ").strip()
            utils.write_config_section(DropboxService.DESCRIPTION.fget(), constants.APP_KEY, app_key)

        if utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.APP_SECRET) == None:
            app_secret = input("Enter your development app secret: ").strip()
            utils.write_config_section(DropboxService.DESCRIPTION.fget(), constants.APP_SECRET, app_secret)

    def backup(self):
        if not self.__has_backup_data():
            print ("No data to backup. Terminated!")
            return
        if not self.__has_backup_folder():
            print ("No destination location for backups. Terminated!")
            return

        file_list = self.__get_backup_data()
        self.__backup(file_list, constants.BACKUP_FOLDER)

    def __has_backup_data(self):
        return utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.BACKUP_DATA) != None

    def __has_backup_folder(self):
        return utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.BACKUP_FOLDER) != None

    ## The path for each file should be separated by a ;
    def __get_backup_data(self):
        raw_list = utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.BACKUP_DATA)
        split_list = raw_list.split(";")
        for idx in range(len(split_list)):
            split_list[idx] = split_list[idx].strip()

        return split_list

    """
    Backups the list of files given by <files>
    """
    def __backup(self, files, dropbox_folder=None):
        for data in files:
            self._put_file(data)

    def _put_file(self, data):
        try:
            with open(data, 'rb') as datafile:
                service_path_raw = utils.get_config_section(DropboxService.DESCRIPTION.fget(), constants.BACKUP_FOLDER)
                normalized_service_path = utils.normalize_folder(service_path_raw)
                final_path = normalized_service_path + utils.get_filename(data)
                print ("File Destination: " + final_path)
                try:
                    # db.put_file(<dest_path>, <object file>, <overwrite>)
                    response = self.dropbox_instance.put_file(final_path, datafile, True)
                    print (data + " was uploaded (" + response['size'] + ")")
                except dbrest.ErrorResponse as e:
                    print ("Error on upload. Skipped file!")
                    print (e)
        except OSError as e:
            print ("Could not open file. Skipped!")
            print (e)
