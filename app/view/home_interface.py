# -*- coding:utf-8 -*-
from datetime import datetime

from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

from qfluentwidgets import qconfig

from ..common.style import AppStyleSheet as ASS

class HomeInterface(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent = parent)
        self.setObjectName('homeInterface')
        self.__init_content()
        self.__init_layout()
        self.__init_qss()
        qconfig.themeChanged.connect(self.__init_qss)
    #
    def __init_content(self):
        self.label_1 = QLabel(self.tr('Welcome to use this RIT Toolkit.'))
        self.label_2 = QLabel()
        self.update_label_2()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label_2)
        self.timer.start(900)
    #
    def update_label_2(self):
        timeReplaceDict = {0:'00', 1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09'}
        now = datetime.now()
        year , month, day = now.year, now.month, now.day
        hour = timeReplaceDict[now.hour] if now.hour < 10 else now.hour
        minute = timeReplaceDict[now.minute] if now.minute < 10 else now.minute
        second = timeReplaceDict[now.second] if now.second < 10 else now.second
        self.label_2.setText(f'Now is {year}-{month}-{day} {hour}:{minute}:{second}')
    #
    def __init_layout(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addStretch()
        layout.addWidget(self.label_1, 0, Qt.AlignCenter)
        layout.addWidget(self.label_2, 0, Qt.AlignCenter)
        layout.addStretch()
    #
    def __init_qss(self):
        with open(ASS.get(ASS.HOME_INTERFACE)) as qssFile:
            self.setStyleSheet(qssFile.read())
