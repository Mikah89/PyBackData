#!/usr/bin/env python

import os

CONF_FILE = os.environ.get("PYBACKDATA_CONF_FILE") or "pybackdata.conf"

AUTH_TOKEN = os.environ.get("PYBACKDATA_AUTH_TOKEN") or "TOKEN"
BACKUP_DATA = os.environ.get("PYBACKDATA_BACKUP_DATA") or "DATA"
BACKUP_FOLDER = os.environ.get("PYBACKDATA_BACKUP_FOLDER") or "BACKUPFOLDER"
APP_KEY = os.environ.get("PYBACKDATA_APP_KEY") or "APPKEY"
APP_SECRET = os.environ.get("PYBACKDATA_APP_SECRET") or "APPSECRET"
