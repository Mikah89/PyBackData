#!/usr/bin/env python

import argparse

import utils
from services.servicefactory import ServiceFactory

def build_arg_list():
    parser = argparse.ArgumentParser()
    parser.add_argument("service", type=str, help="Specifies the backup data service to use")
    return parser

def main():
    parser = build_arg_list()
    args = parser.parse_args()
    ## Create the config file before any operation
    utils.create_config_file()
    service = ServiceFactory.create_service(args.service)
    if service == None:
        print ("The provided service is not supported: " + args.service)
    else:
        service.backup()

if __name__ == "__main__":
    main()
