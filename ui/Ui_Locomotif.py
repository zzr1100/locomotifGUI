# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Locomotif.ui'
#
# Created: Tue Jul 07 07:02:55 2015
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Locomotif(object):
    def setupUi(self, Locomotif):
        Locomotif.setObjectName(_fromUtf8("Locomotif"))
        Locomotif.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Locomotif)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        Locomotif.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Locomotif)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuWindow = QtGui.QMenu(self.menuView)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        Locomotif.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Locomotif)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Locomotif.setStatusBar(self.statusbar)
        self.QuickCommand = QtGui.QDockWidget(Locomotif)
        self.QuickCommand.setFloating(False)
        self.QuickCommand.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickCommand.setObjectName(_fromUtf8("QuickCommand"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cmdLoadFile = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadFile.setObjectName(_fromUtf8("cmdLoadFile"))
        self.verticalLayout.addWidget(self.cmdLoadFile)
        self.cmdLoadProject = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadProject.setObjectName(_fromUtf8("cmdLoadProject"))
        self.verticalLayout.addWidget(self.cmdLoadProject)
        self.QuickCommand.setWidget(self.dockWidgetContents)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickCommand)
        self.actionQuit = QtGui.QAction(Locomotif)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuick_Command_Box = QtGui.QAction(Locomotif)
        self.actionQuick_Command_Box.setObjectName(_fromUtf8("actionQuick_Command_Box"))
        self.actionHelp = QtGui.QAction(Locomotif)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuWindow.addAction(self.actionQuick_Command_Box)
        self.menuView.addAction(self.menuWindow.menuAction())
        self.menuView.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(Locomotif)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Locomotif.close)
        QtCore.QObject.connect(self.actionQuick_Command_Box, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickCommand.show)
        QtCore.QMetaObject.connectSlotsByName(Locomotif)

    def retranslateUi(self, Locomotif):
        Locomotif.setWindowTitle(_translate("Locomotif", "MainWindow", None))
        self.menuFile.setTitle(_translate("Locomotif", "File", None))
        self.menuView.setTitle(_translate("Locomotif", "View", None))
        self.menuWindow.setTitle(_translate("Locomotif", "Window", None))
        self.cmdLoadFile.setText(_translate("Locomotif", "open GPS File", None))
        self.cmdLoadProject.setText(_translate("Locomotif", "open Project", None))
        self.actionQuit.setText(_translate("Locomotif", "Quit", None))
        self.actionQuick_Command_Box.setText(_translate("Locomotif", "Quick Command Box", None))
        self.actionHelp.setText(_translate("Locomotif", "Help", None))

