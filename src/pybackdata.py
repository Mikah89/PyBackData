#!/usr/bin/env python

import cmd
import utils

## TODO Define API
### command "backup" - procedes to backup the data, either by argument or configured in file
### command "chuser" - Changes user and if necessary starts the process of acquiring the token
#### @staticmethod <- static methods
class BackDataTerm(cmd.Cmd):
    pass


def main():
    utils.create_config_file()

if __name__ == "__main__":
    main()
