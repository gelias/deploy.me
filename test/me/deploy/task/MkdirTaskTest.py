import unittest
from mock import Mock
from me.deploy.task.MkdirTask import MkdirTask


class MkdirTaskTest(unittest.TestCase):

    def setUp(self):
        self.commands = Mock()
        self.commands.mk_dir = Mock() 

    def testShouldExecuteMkdirTaskCreatingFolderSuccessfully(self):
        # GIVEN
        self.commands.mk_dir.return_value = True
        need_to_be_created_local_folder = '/tmp/test_folder'
        # WHEN
        mkdir_task = MkdirTask(need_to_be_created_local_folder, self.commands)
        folder_created_successfully = mkdir_task.doTask()
        self.commands.mk_dir.assert_called_once_with('/tmp/test_folder')
        print folder_created_successfully
        # THEN
        self.assertTrue(folder_created_successfully)

if __name__ == "__main__":
    unittest.main()