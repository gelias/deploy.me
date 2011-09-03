class PreDeployment(object):

    def __init__(self, app_name, commands):
        self.app_name = app_name
        self.commands = commands

    def doDownloadAppToDeployment(self):
        download_result = self.commands.download_app(self.app_name)
        return download_result

    
    def buildFoldersOnDeploymentServersBeforeDownloadApp(self):
        folders_built_result = self.commands.build_folders_on_servers()
        return folders_built_result

    
    def uploadAppFileToTheServers(self):
        upload_result = self.commands.upload_app_to_servers(self.app_name, self.commands.app_file_folder_name())
        return upload_result

    
    def start(self):
        download_result = self.doDownloadAppToDeployment()
        build_folders_result = self.buildFoldersOnDeploymentServersBeforeDownloadApp()
        upload_app_result = self.uploadAppFileToTheServers()
        
        return ((download_result == build_folders_result) == upload_app_result)
    
    
    
    
    
    
        