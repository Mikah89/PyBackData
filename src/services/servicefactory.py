#!/usr/bin/env python

from services.dropboxservice import DropboxService

class ServiceFactory():
    @staticmethod
    def create_service(service):
        if service == DropboxService.DESCRIPTION.fget():
            return DropboxService()
        else:
            return None # TODO raise custom exception
