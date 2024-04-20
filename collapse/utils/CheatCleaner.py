from .Logger import logger
from .Selector import selector
import shutil
import os

class CheatCleaner:
    def __init__(self):
        # Absolute path
        self.folders = [
            'C:\\Celestial',
            'C:\\baritone',
            'C:\\shaderpacks',
            'C:\\resourcepacks',
            'C:\\RockAntiLeak',
            'C:\\Rockstar',
            'C:\\MoonProject',
            'C:\\hachrecode',
            'C:\\Nursultan',
        ]

    def scan_folders(self):
        if selector.ask('Remove all cheats folder [y,n]?'):
            for folder in self.folders:
                if os.path.isdir(folder):
                    logger.info('Removing folder: ' + folder)

                    shutil.rmtree(folder, ignore_errors=True)

cheatcleaner = CheatCleaner()