#!/usr/bin/env python

import dropbox

import utils

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
        return ""

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
