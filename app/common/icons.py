
from enum import Enum

from qfluentwidgets import isDarkTheme

from .resource import grp

class LingyunIcon(Enum):
    #
    COUNTER = 'counter'
    #
    def path(self):
        if isDarkTheme():
            return grp(f'app/resource/svg/{self.value}_dark.svg')
        else:
            return grp(f'app/resource/svg/{self.value}_light.svg')