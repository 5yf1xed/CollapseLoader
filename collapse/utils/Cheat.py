import os
from contextlib import chdir

from .Data import data
from .Logger import logger
from .Settings import settings


class Cheat:
    def __init__(self, name: str, link: str, main_class: str = 'net.minecraft.client.main.Main', version: str = '1.12.2', internal: bool = False, use_as_jar: bool = False, use_libraries: bool = True) -> None:
        self.name = name
        self.link = link

        self.filename = os.path.basename(self.link)
        self.path = data.root_dir + self.filename 
        self.path_dir = data.root_dir + os.path.splitext(self.filename)[0] + '/'
        self.jar = os.path.splitext(self.filename)[0] + '.jar'
        
        self.main_class = main_class
        self.version = version
        self.internal = internal
        self.use_as_jar = use_as_jar
        self.use_libraries = use_libraries

    def download(self) -> True:
        """Downloading cheat files"""

        if os.path.isdir(self.path_dir):
            logger.debug(f'Client {self.name} already downloaded')
            return

        logger.debug('Downloading client')

        data.download(self.link)
    
    def run(self):
        """Run client"""
        # Downloading requirements
        data.download('jre-21.0.2.zip')
        data.download('libraries.zip')
        data.download('natives.zip')
        data.download('assets.zip')
        
        logger.info(f'Running client {self.name}')
        with chdir('.\\' + self.path_dir):
            # Using backslash var, because f-strings not supporting it in expressions
            bc = '\\'

            command = f"..\\jre-21.0.2\\bin\\java.exe -noverify -Xmx{settings.get('ram')}M -Djava.library.path={f'..{bc}natives;' if not self.internal and not os.path.isdir(f'natives') else f'.{bc}natives;'} {(f'-cp ..{bc}libraries{bc}*' if not self.internal and not os.path.isdir(f'natives') else f'-cp .{bc}libraries{bc}*' ) + ';' if self.use_libraries else ''}{f'.{bc}' + self.jar + f' {self.main_class}' if not self.use_as_jar else '-jar ' + self.jar} --username {settings.get('nickname')} --gameDir .\\ --assetDir {f'.{bc}assets' if self.internal else f'..{bc}assets'} --assetIndex {self.version} --uuid N/A --accessToken 0 --userType legacy --version {self.version}"

            logger.debug(command)

            os.system(command)

            logger.info('Exited from minecraft')
 