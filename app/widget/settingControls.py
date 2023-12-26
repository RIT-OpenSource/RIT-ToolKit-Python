# -*- coding:utf-8 -*-
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QHBoxLayout

from qfluentwidgets import ExpandGroupSettingCard, PushButton, MessageBox, MessageBoxBase, SubtitleLabel, LineEdit
from qfluentwidgets import FluentIcon as FIF

class CustomExpandGroupSettingCard(ExpandGroupSettingCard):
    pass

class CounterUnitControl(QFrame):
    onDelBtnClicked = pyqtSignal(list)
    def __init__(self, text: str | None = 'Defalut', value: int | None = 0) -> None:
        super().__init__()
        self.text, self.value = text, value
        self.__init_content()
        self.__init_layout()
    #
    def __init_content(self):
        self.textLabel = QLabel(f'{self.text} (Value: {self.value})')
        self.delBtn = PushButton(FIF.REMOVE, 'Remove')
        self.delBtn.clicked.connect(self.__showDelAlertDialog)
    #
    def __showDelAlertDialog(self):
        title = self.tr('Confirm?')
        content = self.tr(f'Are you sure want to delete the "{self.text}"(with value {self.value})？\n⚠ NB! No way to Undo this delete ⚠')
        w = MessageBox(title, content, self.window())
        if w.exec():
            self.onDelBtnClicked.emit([self, self.text])
        else:
            pass
    #
    def __init_layout(self):
        hlayout = QHBoxLayout()
        self.setLayout(hlayout)
        self.setContentsMargins(20, 5, 20, 5)
        hlayout.addWidget(self.textLabel, 0, Qt.AlignLeft | Qt.AlignCenter)
        hlayout.addStretch(1)
        hlayout.addWidget(self.delBtn, 2, Qt.AlignRight | Qt.AlignCenter)

class CustomMessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel(self.tr('Unit Name'), self)
        self.LineEdit = LineEdit(self)
        #
        self.LineEdit.setPlaceholderText(self.tr('Enter the name of the unit'))
        self.LineEdit.setClearButtonEnabled(True)
        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.LineEdit)
        # change the text of button
        self.yesButton.setText(self.tr('Add'))
        self.cancelButton.setText(self.tr('Cancel'))
        self.widget.setMinimumWidth(360)
        self.yesButton.setDisabled(True)
        self.LineEdit.textChanged.connect(self._check)
    def _check(self, text):
        self.yesButton.setEnabled(True if text != None else False)