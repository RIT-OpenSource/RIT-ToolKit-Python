# -*- coding:utf-8 -*-
from enum import Enum
from .resource import grp
from qfluentwidgets import isDarkTheme

class AppStyleSheet(Enum):

    MAIN_WINDOW = 'main_window'
    HOME_INTERFACE = 'home_interface'
    COUNTER_INTERFACE = 'counter_interface'
    COUNTER_CONTROL = 'counter_control'
    COUNTER_CONTROL_RIGHT = 'counter_control_right'

    def get(self):
        type = 'dark' if isDarkTheme() else 'light'
        return grp(f'/app/resource/theme/{type}/{self.value}.qss')