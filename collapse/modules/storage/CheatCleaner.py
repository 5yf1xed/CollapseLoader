import os
import shutil

from ..render.CLI import selector
from ..utils.Module import Module


class CheatCleaner(Module):
    """Cleans cheat folders"""
    def __init__(self) -> None:
        super().__init__()
        self.login = os.getlogin()
        
        if not selector.linux:
            # Absolute path
            self.folders = [
                f'C:\\Users\\{self.login}\\AppData\\Roaming\\.antiautistleak',
                f'C:\\Users\\{self.login}\\.th-client',
                f'C:\\Users\\{self.login}\\.avalon',
                'C:\\shaderpacks',
                'C:\\Rockstar',
                'C:\\RockAntiLeak',
                'C:\\RichRecode'
                'C:\\resourcepacks',
                'C:\\Nursultan',
                'C:\\MoonProject',
                'C:\\hachrecode',
                'C:\\Excellent',
                'C:\\Celestial',
                'C:\\baritone',
                'C:\\hachrecode'
            ]

    def scan_folders(self) -> None:
        """Scans all folders in array, and remove its"""
        if selector.ask('Remove all cheats folder (y,n)?\nall of your configs will be [red bold]ANNIGILATED.[/]'):
            for folder in self.folders:
                if os.path.isdir(folder):
                    self.info('Removing folder: ' + folder)
                    shutil.rmtree(folder, ignore_errors=True)

        selector.pause()

cheatcleaner = CheatCleaner()
