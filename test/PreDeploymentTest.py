import unittest
from PreDeployment import PreDeployment
from mock import Mock

class RequestDeploymentTest(unittest.TestCase):

    def setUp(self):
        self.APP_NAME = 'app.war'
        self.mock_commands = Mock()
        self.mock_commands.download_app = Mock()
        self.mock_commands.build_folders_on_servers = Mock()
        self.mock_commands.upload_app_to_servers = Mock()
        self.mock_commands.app_file_folder_name = Mock()
        self.mock_commands.app_file_folder_name.return_value = '/tmp/'
        
    def testShouldBeAbleCreateANewRequestDeployment(self):
        pre_deployment = PreDeployment(self.APP_NAME, self.mock_commands)
        assert pre_deployment != None, "A new RequestDeployment was not created successfully!"
        
    def testShouldDownloadAppFileFromRepositoryOnceStartedPreDeployment(self):
        # GIVEN 
        self.mock_commands.download_app.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.mock_commands)
        # WHEN
        successfully_downloaded = pre_deployment.doDownloadOfAppToDeployment()
        # THEN
        self.mock_commands.download_app.assert_called_once_with('app.war')
        self.failIf(successfully_downloaded != True, 'The download of app was not performed successfully!')

    def testShouldCreateFoldersOnServersToUploadAppFile(self):
        # GIVEN 
        self.mock_commands.build_folders_on_servers.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.mock_commands)
        # WHEN
        successfully_folders_built = pre_deployment.buildFoldersOnServersToUploadAppFile()
        # THEN
        self.mock_commands.build_folders_on_servers.assert_called_once_with()
        self.failIf(successfully_folders_built != True, 'Folders were not built correctly!')
        
    def testShouldUploadAppFileToTheDeploymentServers(self):
        # GIVEN 
        self.mock_commands.upload_app_to_servers.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.mock_commands)
        # WHEN
        successfully_uploaded = pre_deployment.uploadAppFileToTheServers()
        # THEN
        self.mock_commands.app_file_folder_name.assert_called_once_with()
        self.mock_commands.upload_app_to_servers.assert_called_once_with(self.APP_NAME, '/tmp/')
        self.failIf(successfully_uploaded != True, 'The app.war was not upload to all servers!')
        
    def testShouldDoPreDeploymentOnceStarted(self):
        # GIVEN 
        self.mock_commands.download_app.return_value = True
        self.mock_commands.build_folders_on_servers.return_value = True
        self.mock_commands.upload_app_to_servers.return_value = True
        pre_deployment = PreDeployment(self.APP_NAME, self.mock_commands)
        # WHEN
        successfully_pre_deployed = pre_deployment.start()
        # THEN
        self.mock_commands.app_file_folder_name.assert_called_once_with()
        self.mock_commands.upload_app_to_servers.assert_called_once_with(self.APP_NAME, '/tmp/')
        self.mock_commands.build_folders_on_servers.assert_called_once_with()
        self.mock_commands.download_app.assert_called_once_with('app.war')
        self.failIf(successfully_pre_deployed != True, 'The app.war is not ready to deploy')
                        
        
if __name__ == "__main__":
    unittest.main()