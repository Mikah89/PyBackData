#!/usr/bin/env python

import sys
import os
import stat
import configparser

import constants


config_reader = None

def get_config_dir():
    conf_dir = ""
    if sys.platform.startswith("linux"):
        conf_dir = os.path.expanduser("~/.config/pybackdata/")
    else:
        ## TODO define for windows
        raise Exception("Unknown path for System")

    return conf_dir

def get_config_file():
    return get_config_dir() + constants.CONF_FILE

def config_file_exist():
    conf_file = get_config_dir()
    return os.path.exists(conf_file)

def create_config_file():
    conf_file = get_config_file()
    try:
        os.makedirs(get_config_dir(), stat.S_IRWXU, exist_ok=True)
        # Create file with permission for the ownter to read and write
        conf_file_fd = os.open(conf_file, os.O_CREAT, stat.S_IRUSR | stat.S_IWUSR)
        os.close(conf_file_fd)
    except Exception as err:
        print ("Unable to create configuration file:")
        print (err)

def get_config_reader():
    if config_reader is None and config_file_exist():
        config_reader = configparser.ConfigParser()
        config_reader.read(get_config_file())

    return config_reader

def get_config_section(section_key, config_key):
    reader = get_config_reader()
    if section_key in reader and config_key in reader[section_key]:
        return reader[section_key][config_key]
    else:
        return None

def write_config_section(section_key, config_key, config_value):
    reader = get_config_reader()
    if section_key not in reader:
        reader[section_key] = {config_key: config_value}
    else:
        reader[section_key][config_key] = config_value

    with open(get_config_file(), 'w') as configfile:
        reader.write(configfile)
