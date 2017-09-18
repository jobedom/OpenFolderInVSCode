from fman import DirectoryPaneCommand
from fman import show_alert
import subprocess

class OpenFolderInVSCode(DirectoryPaneCommand):
    def __call__(self):
        subprocess.Popen(['/usr/local/bin/code', self.pane.get_path()], shell=True)
