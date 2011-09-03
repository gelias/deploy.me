'''
Created on Sep 3, 2011

@author: gelias
'''
import unittest
from me.deploy.sys.Commands import Commands
import os

class CommandsTest(unittest.TestCase):

    TMP_FOLDER = "/tmp/test_folder"

    def setUp(self):
        
        self.commands = Commands()
        try:
            os.rmdir(CommandsTest.TMP_FOLDER)
        except:
            print 'SetUp: The tmp folder is unexistent'


    def tearDown(self):
        os.rmdir(CommandsTest.TMP_FOLDER)


    def testShouldMakeDirBasedOnUnixCommandSintax(self):
        # GIVEN
        folder_to_be_created = CommandsTest.TMP_FOLDER
        # WHEN
        folder_created = self.commands.mk_dir(folder_to_be_created)
        # THEN
        self.assertTrue("Should be create the specific folder with no errors", folder_created)

    def testShouldGetOSErrorWhenTryMakeDirAnExistentFolder(self):
        # GIVEN
        os.mkdir(CommandsTest.TMP_FOLDER)
        # WHEN
        folder_already_existent = CommandsTest.TMP_FOLDER
        folder_not_created = self.commands.mk_dir(folder_already_existent)
        # THEN
        self.assertTrue("Should do not created folder because it already exists", not folder_not_created)


if __name__ == "__main__":
    unittest.main()