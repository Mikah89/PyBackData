#!/usr/bin/env python

class Dropbox():

    def __init__(self):
        __init()
        pass

    """
    initializes the service state for use.
    If necessary starts a setup process to obtain the necessary information
    to execute the operations (e.g. service access)
    """
    def __init():
        pass

    """
    Backups the list of files given by <files>
    if an entry of a file is a directory then all files in that directory will be backup up
    if it is a file only that file will be backed up
    """    
    def backup(files, dropbox_folder=None):
        ## TODO support for file filters
        ## TODO support for recursive folder iteration
        pass
