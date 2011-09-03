'''
Created on Sep 3, 2011

@author: gelias
'''
from me.deploy.task.Task import Task

class MkdirTask(Task):
    
    MK_DIR_COMMAND = 'mkdir'
    
    def __init__(self, dir_path, commands):
        self.dir_path = dir_path
        self.commands = commands
        
    def doTask(self):
        return self.commands.mk_dir('/tmp/test_folder')