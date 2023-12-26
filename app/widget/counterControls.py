# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal

from qfluentwidgets import PushButton, PrimaryPushButton, qconfig
from qfluentwidgets import FluentIcon as FIF

from ..common.style import AppStyleSheet as ASS
from ..common.counter import Counter

class CounterControl(QFrame):
    #
    def __init__(self,title=None, default_count=None):
        super().__init__()
        self.title, self.value = title, default_count
        self.setObjectName('CounterFrame')
        self.__init_content()
        self.__init_layout()
        self.__setQss()
        qconfig.themeChanged.connect(self.__setQss)
    #
    def __init_content(self):
        self.titleLabel = QLabel(self.title)
        self.titleLabel.setObjectName('CounterTitleLabel')
        self.conuterRight = _CounterRight(self.value)
        self.conuterRight.onCountChanged.connect(self.__onCountChange)
    #
    def __onCountChange(self, count):
        Counter().set(self.title, count)
    #
    def __init_layout(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 10, 0, 0)
        layout.addWidget(self.titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        layout.addStretch(1)
        layout.addWidget(self.conuterRight, 2, Qt.AlignRight | Qt.AlignVCenter)
        self.setContentsMargins(20, 0, 20, 10)
        self.setMaximumHeight(60)
    #
    def __setQss(self):
        with open(ASS.get(ASS.COUNTER_CONTROL), 'r') as qssFile:
            self.setStyleSheet(qssFile.read())

class _CounterRight(QFrame):
    onCountChanged = pyqtSignal(int)
    #
    def __init__(self, default_count=0):
        super().__init__()
        self.count = default_count
        self.__init_content()
        self.__init_layout()
        self.__setQss()
        qconfig.themeChanged.connect(self.__setQss)
    #
    def __init_content(self):
        self.countLabel = QLabel(str(self.count))
        self.countLabel.setObjectName('CounterRightLabel')
        self.countLabel.setContentsMargins(10, 0, 10, 0)
        self.addBtn = PrimaryPushButton('Add 1', self, FIF.ADD_TO)
        self.minusBtn = PushButton('Minus 1', self, FIF.REMOVE_FROM)
        self.resetBtn = PushButton('Reset', self, FIF.UPDATE)
        self.addBtn.clicked.connect(self.__add_one)
        self.minusBtn.clicked.connect(self.__minus_one)
        self.resetBtn.clicked.connect(self.__reset)
    def __add_one(self):
        self.count += 1
        self.countLabel.setText(str(self.count))
        self.onCountChanged.emit(self.count)
    def __minus_one(self):
        self.count -= 1
        self.countLabel.setText(str(self.count))
        self.onCountChanged.emit(self.count)
    def __reset(self):
        self.count = 0 
        self.countLabel.setText(str(self.count))
        self.onCountChanged.emit(self.count)
    #
    def __init_layout(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.addBtn, 0, Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(self.countLabel, 0, Qt.AlignCenter)
        layout.addWidget(self.minusBtn, 0, Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.resetBtn, 0, Qt.AlignRight | Qt.AlignVCenter)
    #
    def __setQss(self):
        with open(ASS.get(ASS.COUNTER_CONTROL_RIGHT), 'r') as qssFile:
            self.setStyleSheet(qssFile.read())