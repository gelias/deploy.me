import unittest
from mock import Mock
from me.deploy.pre.PreDeployment import PreDeployment

class RequestDeploymentTest(unittest.TestCase):

    def setUp(self):
        self.APP_NAME = 'app.war'
        self.mkdir_task_one = Mock()
        self.mkdir_task_one.doTask = Mock()
        self.mkdir_task_two = Mock()
        self.mkdir_task_two.doTask = Mock()
        
    def testShouldBeAbleCreateANewPreDeploymentRequest(self):
        pre_deployment = PreDeployment([])
        assert pre_deployment != None, "A new PreDeploymentRequest was not created successfully!"
        
    def testShouldRunPreDeploymentOnceHavingListOfMkdirTasksSuccessfully(self):
        # GIVEN
        self.mkdir_task_one.doTask.return_value = True
        self.mkdir_task_two.doTask.return_value = True
        pre_deploy_task_list = [self.mkdir_task_one, self.mkdir_task_one]
        pre_deployment = PreDeployment(pre_deploy_task_list)
        # WHEN
        ran_successfully = pre_deployment.run()
        # THEN
        self.mkdir_task_one.doTask.assert_called_once
        self.mkdir_task_two.doTask.assert_called_once
        self.assertTrue("A new PreDeploymentRequest was not created successfully!", ran_successfully)

    def testShouldFailOnRunPreDeploymentWhenRunSecondTask(self):
        # GIVEN
        self.mkdir_task_one.doTask.return_value = True
        self.mkdir_task_two.doTask.return_value = False
        pre_deploy_task_list = [self.mkdir_task_one, self.mkdir_task_one]
        pre_deployment = PreDeployment(pre_deploy_task_list)
        # WHEN
        ran_successfully = pre_deployment.run()
        # THEN
        self.mkdir_task_one.doTask.assert_called_once
        self.mkdir_task_two.doTask.call_count == 0
        self.assertTrue("A new PreDeploymentRequest was not created successfully!", ran_successfully)        
        
if __name__ == "__main__":
    unittest.main()