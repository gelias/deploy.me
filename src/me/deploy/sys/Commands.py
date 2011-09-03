'''
Created on Jul 14, 2011

@author: gelias
'''
import os

class Commands(object):
        
    def upload_app_to_servers(self, app_name, folder):
        pass
    
    def download_app(self, app_name):
        pass
    
    def mk_dir(self, path_to_be_created):
        self.created = False
        try:
            os.mkdir(path_to_be_created)
            self.created = os.access(path_to_be_created, os.R_OK)
            return self.created
        except OSError:
            print("Error: " + path_to_be_created + " was not created. Check the path")
            
        return self.created
            