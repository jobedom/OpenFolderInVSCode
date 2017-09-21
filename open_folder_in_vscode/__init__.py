from fman import DirectoryPaneCommand
from subprocess import Popen

class OpenFolderInVSCode(DirectoryPaneCommand):
    def __call__(self):
        path = self.pane.get_path()
        Popen('/usr/local/bin/code "%s"' % path, shell=True)
