# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Locomotif.ui'
#
# Created: Wed Aug 05 00:23:51 2015
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
        Locomotif.resize(1109, 767)
        Locomotif.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 232);"))
        self.centralwidget = QtGui.QWidget(Locomotif)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mainDataDisplay = QtGui.QTabWidget(self.centralwidget)
        self.mainDataDisplay.setEnabled(True)
        self.mainDataDisplay.setGeometry(QtCore.QRect(0, 0, 971, 691))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainDataDisplay.sizePolicy().hasHeightForWidth())
        self.mainDataDisplay.setSizePolicy(sizePolicy)
        self.mainDataDisplay.setSizeIncrement(QtCore.QSize(10, 10))
        self.mainDataDisplay.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 232);"))
        self.mainDataDisplay.setTabPosition(QtGui.QTabWidget.North)
        self.mainDataDisplay.setTabShape(QtGui.QTabWidget.Rounded)
        self.mainDataDisplay.setTabsClosable(True)
        self.mainDataDisplay.setMovable(True)
        self.mainDataDisplay.setObjectName(_fromUtf8("mainDataDisplay"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.label_2 = QtGui.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.t1LoadedDataFilename = QtGui.QLineEdit(self.tab_1)
        self.t1LoadedDataFilename.setGeometry(QtCore.QRect(80, 20, 531, 20))
        self.t1LoadedDataFilename.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1LoadedDataFilename.setObjectName(_fromUtf8("t1LoadedDataFilename"))
        self.label_3 = QtGui.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.t1LoadedDatasets = QtGui.QLineEdit(self.tab_1)
        self.t1LoadedDatasets.setGeometry(QtCore.QRect(80, 50, 531, 20))
        self.t1LoadedDatasets.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1LoadedDatasets.setObjectName(_fromUtf8("t1LoadedDatasets"))
        self.t1Data = QtGui.QTabWidget(self.tab_1)
        self.t1Data.setGeometry(QtCore.QRect(20, 90, 951, 571))
        self.t1Data.setObjectName(_fromUtf8("t1Data"))
        self.t11Data = QtGui.QWidget()
        self.t11Data.setObjectName(_fromUtf8("t11Data"))
        self.t1Data.addTab(self.t11Data, _fromUtf8(""))
        self.t12Polygon = QtGui.QWidget()
        self.t12Polygon.setObjectName(_fromUtf8("t12Polygon"))
        self.t1Data.addTab(self.t12Polygon, _fromUtf8(""))
        self.t13Polygon = QtGui.QWidget()
        self.t13Polygon.setObjectName(_fromUtf8("t13Polygon"))
        self.t1Data.addTab(self.t13Polygon, _fromUtf8(""))
        self.t14Map = QtGui.QWidget()
        self.t14Map.setObjectName(_fromUtf8("t14Map"))
        self.t14MapView = QtGui.QGraphicsView(self.t14Map)
        self.t14MapView.setGeometry(QtCore.QRect(0, 0, 951, 551))
        self.t14MapView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t14MapView.setObjectName(_fromUtf8("t14MapView"))
        self.t1Data.addTab(self.t14Map, _fromUtf8(""))
        self.t15Map = QtGui.QWidget()
        self.t15Map.setObjectName(_fromUtf8("t15Map"))
        self.t15MapView = QtGui.QGraphicsView(self.t15Map)
        self.t15MapView.setGeometry(QtCore.QRect(0, 0, 951, 551))
        self.t15MapView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t15MapView.setObjectName(_fromUtf8("t15MapView"))
        self.t1Data.addTab(self.t15Map, _fromUtf8(""))
        self.mainDataDisplay.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.mainDataDisplay.addTab(self.tab_2, _fromUtf8(""))
        Locomotif.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Locomotif)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 21))
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
        self.QuickCommand.setMinimumSize(QtCore.QSize(120, 139))
        self.QuickCommand.setMaximumSize(QtCore.QSize(524287, 176))
        self.QuickCommand.setAcceptDrops(True)
        self.QuickCommand.setAutoFillBackground(False)
        self.QuickCommand.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.QuickCommand.setFloating(False)
        self.QuickCommand.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickCommand.setObjectName(_fromUtf8("QuickCommand"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.formLayout = QtGui.QFormLayout(self.dockWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cmdLoadDataFile = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadDataFile.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdLoadDataFile.setObjectName(_fromUtf8("cmdLoadDataFile"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.cmdLoadDataFile)
        self.cmdLoadGPSFile = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadGPSFile.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdLoadGPSFile.setObjectName(_fromUtf8("cmdLoadGPSFile"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.cmdLoadGPSFile)
        self.cmdLoadProject = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadProject.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdLoadProject.setObjectName(_fromUtf8("cmdLoadProject"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.cmdLoadProject)
        self.QuickCommand.setWidget(self.dockWidgetContents)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickCommand)
        self.QuickStatus = QtGui.QDockWidget(Locomotif)
        self.QuickStatus.setMinimumSize(QtCore.QSize(120, 38))
        self.QuickStatus.setAutoFillBackground(False)
        self.QuickStatus.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QuickStatus.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickStatus.setObjectName(_fromUtf8("QuickStatus"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.label = QtGui.QLabel(self.dockWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.loadedDataFilename = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.loadedDataFilename.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.loadedDataFilename.setObjectName(_fromUtf8("loadedDataFilename"))
        self.cmdReadCSV = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdReadCSV.setGeometry(QtCore.QRect(10, 60, 101, 23))
        self.cmdReadCSV.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdReadCSV.setObjectName(_fromUtf8("cmdReadCSV"))
        self.cmdCreateCluster = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdCreateCluster.setGeometry(QtCore.QRect(10, 90, 101, 23))
        self.cmdCreateCluster.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdCreateCluster.setObjectName(_fromUtf8("cmdCreateCluster"))
        self.cmdCreateVPolygone = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdCreateVPolygone.setGeometry(QtCore.QRect(10, 120, 101, 23))
        self.cmdCreateVPolygone.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdCreateVPolygone.setObjectName(_fromUtf8("cmdCreateVPolygone"))
        self.cmdCreateMaps = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdCreateMaps.setGeometry(QtCore.QRect(10, 230, 101, 23))
        self.cmdCreateMaps.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdCreateMaps.setObjectName(_fromUtf8("cmdCreateMaps"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cmdMapWidth = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.cmdMapWidth.setGeometry(QtCore.QRect(10, 200, 41, 20))
        self.cmdMapWidth.setObjectName(_fromUtf8("cmdMapWidth"))
        self.cmdMapHeight = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.cmdMapHeight.setGeometry(QtCore.QRect(60, 200, 41, 20))
        self.cmdMapHeight.setObjectName(_fromUtf8("cmdMapHeight"))
        self.QuickStatus.setWidget(self.dockWidgetContents_2)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickStatus)
        self.actionQuit = QtGui.QAction(Locomotif)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuick_Command_Box = QtGui.QAction(Locomotif)
        self.actionQuick_Command_Box.setChecked(False)
        self.actionQuick_Command_Box.setObjectName(_fromUtf8("actionQuick_Command_Box"))
        self.actionHelp = QtGui.QAction(Locomotif)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionOpen_GPS_File = QtGui.QAction(Locomotif)
        self.actionOpen_GPS_File.setObjectName(_fromUtf8("actionOpen_GPS_File"))
        self.actionOpen_Project = QtGui.QAction(Locomotif)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionStatus_Box = QtGui.QAction(Locomotif)
        self.actionStatus_Box.setChecked(False)
        self.actionStatus_Box.setObjectName(_fromUtf8("actionStatus_Box"))
        self.menuFile.addAction(self.actionOpen_GPS_File)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuWindow.addAction(self.actionQuick_Command_Box)
        self.menuWindow.addAction(self.actionStatus_Box)
        self.menuView.addAction(self.menuWindow.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(Locomotif)
        self.mainDataDisplay.setCurrentIndex(0)
        self.t1Data.setCurrentIndex(4)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Locomotif.close)
        QtCore.QObject.connect(self.actionQuick_Command_Box, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickCommand.show)
        QtCore.QObject.connect(self.actionStatus_Box, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickStatus.show)
        QtCore.QObject.connect(self.actionOpen_Project, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openProjectFile)
        QtCore.QObject.connect(self.cmdLoadGPSFile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openGPSFile)
        QtCore.QObject.connect(self.cmdLoadProject, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openProjectFile)
        QtCore.QObject.connect(self.actionOpen_GPS_File, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openGPSFile)
        QtCore.QObject.connect(self.cmdLoadDataFile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openDataFile)
        QtCore.QObject.connect(self.cmdCreateMaps, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doCreateMaps)
        QtCore.QObject.connect(self.cmdReadCSV, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doReadCSV)
        QtCore.QObject.connect(self.cmdCreateCluster, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doCreateCluster)
        QtCore.QObject.connect(self.cmdCreateVPolygone, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doCreatePolygone)
        QtCore.QMetaObject.connectSlotsByName(Locomotif)

    def retranslateUi(self, Locomotif):
        Locomotif.setWindowTitle(_translate("Locomotif", "MainWindow", None))
        self.label_2.setText(_translate("Locomotif", "Datendatei:", None))
        self.label_3.setText(_translate("Locomotif", "Datasets:", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t11Data), _translate("Locomotif", "Daten", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t12Polygon), _translate("Locomotif", "Polygon1", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t13Polygon), _translate("Locomotif", "Polygon2", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t14Map), _translate("Locomotif", "Map1", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t15Map), _translate("Locomotif", "Map2", None))
        self.mainDataDisplay.setTabText(self.mainDataDisplay.indexOf(self.tab_1), _translate("Locomotif", "Tab 1", None))
        self.mainDataDisplay.setTabText(self.mainDataDisplay.indexOf(self.tab_2), _translate("Locomotif", "Tab 2", None))
        self.menuFile.setTitle(_translate("Locomotif", "File", None))
        self.menuView.setTitle(_translate("Locomotif", "View", None))
        self.menuWindow.setTitle(_translate("Locomotif", "Window", None))
        self.QuickCommand.setWhatsThis(_translate("Locomotif", "<html><head/><body><p>Bla Bla ...</p></body></html>", None))
        self.QuickCommand.setWindowTitle(_translate("Locomotif", "Commands", None))
        self.cmdLoadDataFile.setText(_translate("Locomotif", "open Data File", None))
        self.cmdLoadGPSFile.setText(_translate("Locomotif", "open GPS File", None))
        self.cmdLoadProject.setText(_translate("Locomotif", "open Project", None))
        self.QuickStatus.setWindowTitle(_translate("Locomotif", "Bearbeiten", None))
        self.label.setText(_translate("Locomotif", "Datendatei", None))
        self.cmdReadCSV.setText(_translate("Locomotif", "CSV einlesen", None))
        self.cmdCreateCluster.setText(_translate("Locomotif", "Cluster erstellen", None))
        self.cmdCreateVPolygone.setText(_translate("Locomotif", "V-Polygone ber.", None))
        self.cmdCreateMaps.setText(_translate("Locomotif", "Erstellen", None))
        self.label_4.setText(_translate("Locomotif", "Karten:", None))
        self.actionQuit.setText(_translate("Locomotif", "Quit", None))
        self.actionQuick_Command_Box.setText(_translate("Locomotif", "Quick Command Box", None))
        self.actionHelp.setText(_translate("Locomotif", "Help", None))
        self.actionOpen_GPS_File.setText(_translate("Locomotif", "Open GPS File...", None))
        self.actionOpen_Project.setText(_translate("Locomotif", "Open Project...", None))
        self.actionStatus_Box.setText(_translate("Locomotif", "Status Box", None))
