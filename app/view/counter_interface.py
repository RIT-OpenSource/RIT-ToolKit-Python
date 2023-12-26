# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from qfluentwidgets import qconfig

from ..widget.counterControls import CounterControl
from ..common.style import AppStyleSheet as ASS
from ..common.counter import Counter

class CounterInterface(QFrame):
    ''' Blank Interface '''
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setObjectName('counterInterface')
        self.list = Counter().getall()
        self.__init_layout()
        self.__init_content()
        self.__init_qss()
        qconfig.themeChanged.connect(self.__init_qss)
    #
    def __init_layout(self):
        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)
        self.vlayout.setContentsMargins(36, 30, 36, 0)
    #
    def __init_content(self):
        title = QLabel('Counter')
        title.setObjectName('counterInterfaceTitle')
        title.setContentsMargins(0, 20, 0, 0)
        self.vlayout.addWidget(title, 0, Qt.AlignTop)
        self.vlayout.addSpacing(10)
        for i in range(len(self.list)):
            item = self.list[i]
            itemName = item['name']
            itemValue = item['value']
            self.vlayout.addWidget(CounterControl(itemName, itemValue), 0, Qt.AlignTop)
        self.vlayout.addStretch(1)
    #
    def __init_qss(self):
        with open(ASS.get(ASS.COUNTER_INTERFACE)) as qssFile:
            self.setStyleSheet(qssFile.read())
