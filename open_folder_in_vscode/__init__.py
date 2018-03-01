from fman import DirectoryPaneCommand
from fman.url import as_human_readable
from subprocess import Popen
import os.path


class OpenFolderInVSCode(DirectoryPaneCommand):
    default_exe_path = 'code'
    unix_exe_path = '/usr/local/bin/code'

    def __call__(self):
        path = self.pane.get_path()
        # Convert path to one that the OS should understand (stripping 'file://' prefix and normalizing the path separator).
        path = as_human_readable(path)
        exe_path = self.get_exe_path()
        Popen('{} "{}"'.format(exe_path, path), shell=True)

    def get_exe_path(self):
        # Use (default?) unix path if it exists
        if os.path.isfile(self.unix_exe_path):
            return self.unix_exe_path
        return self.default_exe_path
