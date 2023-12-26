# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

from qfluentwidgets import SettingCardGroup, ScrollArea, ExpandLayout, HyperlinkCard
from qfluentwidgets import FluentIcon as FIF

from ..common.config import Constants

class InformationInterface(ScrollArea):
    """ Setting interface """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        #
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        # setting label
        self.informationLabel = QLabel(self.tr("Information"), self)
        self.informationLabel.setContentsMargins(0, 20, 0, 0)
        # application
        self.aboutGroup = SettingCardGroup(self.tr('About'), self.scrollWidget)
        self.aboutCard = HyperlinkCard(
            Constants.RELEASE_URL.value,
            self.tr('Check update'),
            FIF.INFO,
            self.tr('About'),
            f"© {self.tr('Copyright') } {Constants.YEAR.value}, {Constants.AUTHOR.value}. {self.tr('Version')} {Constants.PACKAGE_VERSION.value}",
            self.aboutGroup
        )
        self.__initWidget()
    #
    #
    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 100, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName('informationInterface')
        # initialize style sheet
        self.scrollWidget.setObjectName('scrollWidget')
        self.informationLabel.setObjectName('settingLabel')
        # initialize layout
        self.__initLayout()
    #
    def __initLayout(self):
        self.informationLabel.move(36, 30)
        # add cards to group
        self.aboutGroup.addSettingCards([self.aboutCard])
        # add setting card group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.aboutGroup)