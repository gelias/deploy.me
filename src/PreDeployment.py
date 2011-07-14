import os

class PreDeployment(object):

    def __init__(self, app_name):
        self.app_name = app_name

    def start(self):
        os.system('/tmp/script_ftp.sh %s' % self.app_name)
        f=os.popen("ftp_script.log")
        output = ""
        for i in f.readlines():
            output += i
        return output
        