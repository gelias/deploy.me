class PreDeployment(object):

    def __init__(self, task_list):
        self.task_list = task_list

    def run(self):
        for task in self.task_list:
            if not(task.doTask()):
                return False
        
        return True