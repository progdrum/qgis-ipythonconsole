# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Settings.ui'
#
# Created: Tue Apr 21 12:47:10 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(956, 612)
        self.gridLayout_2 = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setAccessibleName(_fromUtf8(""))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.windowModeFloating = QtGui.QRadioButton(self.groupBox)
        self.windowModeFloating.setObjectName(_fromUtf8("windowModeFloating"))
        self.verticalLayout_5.addWidget(self.windowModeFloating)
        self.windowModeDocked = QtGui.QRadioButton(self.groupBox)
        self.windowModeDocked.setObjectName(_fromUtf8("windowModeDocked"))
        self.verticalLayout_5.addWidget(self.windowModeDocked)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.fontSize = QtGui.QSpinBox(self.tab)
        self.fontSize.setMinimum(6)
        self.fontSize.setMaximum(40)
        self.fontSize.setProperty("value", 10)
        self.fontSize.setObjectName(_fromUtf8("fontSize"))
        self.gridLayout.addWidget(self.fontSize, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings", None))
        self.groupBox.setTitle(_translate("SettingsDialog", "Default window mode", None))
        self.windowModeFloating.setText(_translate("SettingsDialog", "floating", None))
        self.windowModeDocked.setText(_translate("SettingsDialog", "docked", None))
        self.label_2.setText(_translate("SettingsDialog", "Console font size", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "Settings", None))
        self.label.setText(_translate("SettingsDialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">IPython QGIS Console </span></p><p>An IPython interactive console with batteries included. </p><p><a href=\"http://www.itopen.it\"><span style=\" text-decoration: underline; color:#0057ae;\">IPyConsole home page</span></a></p><p><a href=\"http://www.ipython.org\"><span style=\" text-decoration: underline; color:#0057ae;\">IPython project page</span></a> (feed-back is highly appreciated!)</p><p><a href=\"https://github.com/elpaso/qgis-ipythonconsole\"><span style=\" text-decoration: underline; color:#0057ae;\">Plugin source code and bug tracker</span></a></p><p>Do you like IPyConsole? Make a <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XEXYSQAQQYZGS\"><span style=\" text-decoration: underline; color:#0057ae;\">small donation</span></a> to keep this project alive! <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XEXYSQAQQYZGS\"><img src=\":/plugins/IPyConsole/icons/paypal.png\"/></a></p></body></html>", None))
        self.label_3.setText(_translate("SettingsDialog", "<html><head/><body><p><img src=\":/plugins/IPyConsole/icons/icon.png\"/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "About", None))

import resources_rc
