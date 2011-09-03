'''
Created on Jul 14, 2011

@author: gelias
'''

class DeploymentExecutor(object):

    def __init__(self, deployment_request):
        self.deployment_request = deployment_request

    def doPreDeployment(self):
        pre_deployment_result = self.deployment_request.runPredeployment()
        return pre_deployment_result
    
    
        