import unittest
from mock import Mock
from me.deploy.pre.PreDeployment import PreDeployment
from me.deploy.task.MkdirTask import MkdirTask



class RequestDeploymentTest(unittest.TestCase):

    def setUp(self):
        self.APP_NAME = 'app.war'
        self.commands = Mock()
        self.commands.download_app = Mock()
        self.commands.build_folders_on_servers = Mock()
        self.commands.upload_app_to_servers = Mock()
        self.commands.app_file_folder_name = Mock()
        self.commands.app_file_folder_name.return_value = '/tmp/'
        
    def testShouldBeAbleCreateANewPreDeploymentRequest(self):
        pre_deployment = PreDeployment(self.APP_NAME, self.commands)
        assert pre_deployment != None, "A new PreDeploymentRequest was not created successfully!"
        
    def ShouldCreateFoldersOnDeploymentServerBeforeDownloadApp(self):
        # GIVEN 
        self.commands.build_folders_on_servers.return_value = True
        # pre_deployment = PreDeployment(self.APP_NAME, self.commands)
        downloadAppTask = MkdirTask("", self.commands);
        pre_deployment = PreDeployment(self.APP_NAME, self.commands)
        # WHEN
        successfully_folders_built = pre_deployment.executeTasks()
        # THEN
        self.commands.build_folders_on_servers.assert_called_once_with()
        self.failIf(successfully_folders_built != True, 'Folders were not built correctly!')        
        
    def testShouldDownloadAppFileFromCIServer(self):
        # GIVEN 
        self.commands.download_app.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.commands)
        # WHEN
        successfully_downloaded = pre_deployment.doDownloadAppToDeployment()
        # THEN
        self.commands.download_app.assert_called_once_with('app.war')
        self.failIf(successfully_downloaded != True, 'The download of the app app.war was not performed successfully!')
        
    def testShouldCreateFoldersOnRemoteServersBeforeDispatchAppFile(self):
        # GIVEN 
        self.commands.upload_app_to_servers.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.commands)
        # WHEN
        successfully_uploaded = pre_deployment.uploadAppFileToTheServers()
        # THEN
        self.commands.app_file_folder_name.assert_called_once_with()
        self.commands.upload_app_to_servers.assert_called_once_with(self.APP_NAME, '/tmp/')
        self.failIf(successfully_uploaded != True, 'The app.war was not upload to all servers!')
        
    def testShouldDoPreDeploymentOnceStarted(self):
        # GIVEN 
        self.commands.download_app.return_value = True
        self.commands.build_folders_on_servers.return_value = True
        self.commands.upload_app_to_servers.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.commands)
        # WHEN
        successfully_pre_deployed = pre_deployment.start()
        # THEN
        self.commands.app_file_folder_name.assert_called_once_with()
        self.commands.upload_app_to_servers.assert_called_once_with(self.APP_NAME, '/tmp/')
        self.commands.build_folders_on_servers.assert_called_once_with()
        self.commands.download_app.assert_called_once_with('app.war')
        self.failIf(successfully_pre_deployed != True, 'The app.war is not ready to deploy')
                        
        
if __name__ == "__main__":
    unittest.main()