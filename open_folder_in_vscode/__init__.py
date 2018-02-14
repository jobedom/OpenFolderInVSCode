from fman import DirectoryPaneCommand
from fman.url import as_human_readable
from subprocess import Popen
import os.path


class OpenFolderInVSCode(DirectoryPaneCommand):
    default_exe_path = 'code'
    unix_exe_path = '/usr/local/bin/code'

    def __call__(self):
        paths = self.get_file_paths()
        exe_path = self.get_exe_path()

        args = [exe_path]
        args.extend(paths)
        Popen(args, shell=True)

    def get_file_paths(self):
        selection = self.pane.get_selected_files()
        if selection:
            return [as_human_readable(p) for p in selection]
        return [as_human_readable(self.pane.get_path())]

    def get_exe_path(self):
        # Use (default?) unix path if it exists
        if os.path.isfile(self.unix_exe_path):
            return self.unix_exe_path
        return self.default_exe_path
