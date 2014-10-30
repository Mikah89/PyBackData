#!/usr/bin/env python

import sys
import os
import stat
import configparser

import constants



def get_config_dir():
    conf_dir = ""
    if sys.platform.startswith("linux"):
        conf_dir = os.path.expanduser("~/.config/pybackdata/")
    else:
        ## TODO define for windows
        raise Exception("Unknown path for System")

    return conf_dir

def get_config_file():
    return get_config_dir() + constants.CONF_FILE;

def config_file_exist():
    conf_file = get_config_dir()
    return os.path.exists(conf_file)

## TODO logs
def create_config_file():
    conf_file = get_config_file();
    try:
        os.makedirs(get_config_dir(), stat.S_IRWXU, exist_ok=True)
        # Create file with permission for the ownter to read and write
        conf_file_fd = os.open(conf_file, os.O_CREAT, stat.S_IRUSR | stat.S_IWUSR)
        os.close(conf_file_fd)
    except Exception as err:
        print ("Unable to create configuration file:")
        print (err)

def config_reader():
    config_reader = None
    if config_reader is None and config_file_exist():
        config_reader = configparser.ConfigParser()
        config_reader.read(get_config_file())

    return config_reader;
