'''
Created on Sep 3, 2011

@author: gelias
'''
from me.deploy.task.Task import Task

class MkdirTask(Task):
    
    def __init__(self, dir_path, commands):
        Task.__init__(self, commands)
        self.dir_path = dir_path
        self.commands = commands
        
    def doTask(self):
        self.commands.mk_dir('mkdir ' + self.dir_path)