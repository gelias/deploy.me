import unittest
from PreDeployment import PreDeployment


class RequestDeploymentTest(unittest.TestCase):

    def setUp(self):
        self.APP_NAME = 'app.war'
        
    def testShouldBeAbleCreateANewRequestDeployment(self):
        pre_deployment = PreDeployment(self.APP_NAME)
        assert pre_deployment != None, "A new RequestDeployment was not created successfully!"
        
    def testShouldDownloadAppFileFromRepositoryOnceStartedPreDeployment(self):
        # GIVEN 
        pre_deployment = PreDeployment(self.APP_NAME)
        # WHEN
        pre_deploy_output = pre_deployment.start()
        # THEN
        assert pre_deploy_output == 'app.war downloaded successfully!', 'Pre deployment failed'
        
        
if __name__ == "__main__":
    unittest.main()