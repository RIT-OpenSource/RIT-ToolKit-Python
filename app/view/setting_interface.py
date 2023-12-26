# -*- coding:utf-8 -*-
import functools

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

from qfluentwidgets import (SettingCardGroup, OptionsSettingCard, PushButton,
                            ScrollArea, ExpandLayout, InfoBar, setTheme,)
from qfluentwidgets import FluentIcon as FIF

from ..common.Lib.g_config import cfg
from ..common.counter import Counter
from ..common.icons import LingyunIcon as LYI

from ..widget.settingControls import CustomExpandGroupSettingCard as CEGSC, CounterUnitControl, CustomMessageBox as CMB

class SettingInterface(ScrollArea):
    """ Setting interface """
    def __init__(self, parent=None, QssEditFunction=None):
        super().__init__(parent=parent)
        # Get Qss EditFunction
        self.QssEditFunction = QssEditFunction
        #
        self.unitList = []
        #
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        # setting label
        self.settingLabel = QLabel(self.tr("Settings"), self)
        self.settingLabel.setContentsMargins(0, 20, 0, 0)
        # counter
        self.counterGroup = SettingCardGroup(self.tr('Counter'), self.scrollWidget)
        self.counterCard = CEGSC(
            LYI.path(LYI.COUNTER),
            self.tr('Counter'),
            self.tr('Add, Edit or Remove Counter Unit Here')
        )
        addBtn = PushButton(FIF.ADD, self.tr('Add Counter'))
        addBtn.clicked.connect(self.__onAdd)
        self.counterCard.addWidget(addBtn)
        self.__init_counter_card()
        # personalization
        self.personalGroup = SettingCardGroup(self.tr('Personalization'), self.scrollWidget)
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.tr('Application theme'),
            self.tr("Change the appearance of your application"),
            texts=[
                self.tr('Light'), self.tr('Dark'),
                self.tr('Use system setting')
            ],
            parent=self.personalGroup
        )
        self.__initWidget()
    #
    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 100, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')
        # initialize style sheet
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')
        # initialize layout
        self.__initLayout()
        self.__connectSignalToSlot()
    #
    def __initLayout(self):
        self.settingLabel.move(36, 30)
        # add cards to group
        self.counterGroup.addSettingCard(self.counterCard)
        self.personalGroup.addSettingCard(self.themeCard)
        # add setting card group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.counterGroup)
        self.expandLayout.addWidget(self.personalGroup)
    #
    def __showRestartTooltip(self):
        InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Some parts will takes effect after restart'),
            duration=1500,
            parent=self
        )
    def __showRebootTooltip(self):
        w = InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Change will takes effect after restart'),
            duration=5000,
            parent=self
        )
    #
    def __connectSignalToSlot(self):
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        # personalization
        self.themeCard.optionChanged.connect(self.__settheme)
    #
    def __init_counter_card(self):
        CounterList = Counter().getall()
        for counter in CounterList:
            name = counter['name']
            value = counter['value']
            counterUnit = CounterUnitControl(name, value)
            self.counterCard.addGroupWidget(counterUnit)
            onDelPartial = functools.partial(self.__onDel, name)
            counterUnit.onDelBtnClicked.connect(onDelPartial)
    #
    def __onAdd(self):
        w = CMB(self.window())
        if w.exec():
            text = w.LineEdit.text()
            Counter().join(text, 0)
            self.__showRebootTooltip()
    #
    def __onDel(self, arg):
        Counter().remove(arg)
        self.__showRebootTooltip()
    #
    def __settheme(self, ci):
        setTheme(cfg.get(ci))
        self.QssEditFunction()
        self.__showRestartTooltip()