# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Locomotif.ui'
#
# Created: Fri Aug 28 15:43:39 2015
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
        Locomotif.resize(1168, 751)
        Locomotif.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 232);"))
        self.centralwidget = QtGui.QWidget(Locomotif)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mainDataDisplay = QtGui.QTabWidget(self.centralwidget)
        self.mainDataDisplay.setEnabled(True)
        self.mainDataDisplay.setGeometry(QtCore.QRect(0, 0, 991, 701))
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
        self.t1Data.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.t1Data.setObjectName(_fromUtf8("t1Data"))
        self.t1FileData = QtGui.QWidget()
        self.t1FileData.setObjectName(_fromUtf8("t1FileData"))
        self.t1FileDataView = QtGui.QTableWidget(self.t1FileData)
        self.t1FileDataView.setGeometry(QtCore.QRect(0, 0, 941, 551))
        self.t1FileDataView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.t1FileDataView.setLineWidth(1)
        self.t1FileDataView.setAlternatingRowColors(False)
        self.t1FileDataView.setShowGrid(True)
        self.t1FileDataView.setRowCount(10)
        self.t1FileDataView.setColumnCount(6)
        self.t1FileDataView.setObjectName(_fromUtf8("t1FileDataView"))
        self.t1Data.addTab(self.t1FileData, _fromUtf8(""))
        self.t1GoogleMaps = QtGui.QWidget()
        self.t1GoogleMaps.setObjectName(_fromUtf8("t1GoogleMaps"))
        self.t1GoogleMapsView = QtWebKit.QWebView(self.t1GoogleMaps)
        self.t1GoogleMapsView.setGeometry(QtCore.QRect(100, 20, 843, 526))
        self.t1GoogleMapsView.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.t1GoogleMapsView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.t1GoogleMapsView.setObjectName(_fromUtf8("t1GoogleMapsView"))
        self.t1GoogleMapsHint = QtGui.QLabel(self.t1GoogleMaps)
        self.t1GoogleMapsHint.setGeometry(QtCore.QRect(0, 0, 947, 20))
        self.t1GoogleMapsHint.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);"))
        self.t1GoogleMapsHint.setText(_fromUtf8(""))
        self.t1GoogleMapsHint.setObjectName(_fromUtf8("t1GoogleMapsHint"))
        self.t1GMmaptype = QtGui.QRadioButton(self.t1GoogleMaps)
        self.t1GMmaptype.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.t1GMmaptype.setChecked(True)
        self.t1GMmaptype.setAutoExclusive(True)
        self.t1GMmaptype.setObjectName(_fromUtf8("t1GMmaptype"))
        self.t1GMmaptype_2 = QtGui.QRadioButton(self.t1GoogleMaps)
        self.t1GMmaptype_2.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.t1GMmaptype_2.setObjectName(_fromUtf8("t1GMmaptype_2"))
        self.t1GMmaptype_3 = QtGui.QRadioButton(self.t1GoogleMaps)
        self.t1GMmaptype_3.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.t1GMmaptype_3.setObjectName(_fromUtf8("t1GMmaptype_3"))
        self.t1GMmaptype_4 = QtGui.QRadioButton(self.t1GoogleMaps)
        self.t1GMmaptype_4.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.t1GMmaptype_4.setObjectName(_fromUtf8("t1GMmaptype_4"))
        self.label_9 = QtGui.QLabel(self.t1GoogleMaps)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.t1GMMapWidth = QtGui.QLineEdit(self.t1GoogleMaps)
        self.t1GMMapWidth.setGeometry(QtCore.QRect(10, 170, 31, 20))
        self.t1GMMapWidth.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1GMMapWidth.setText(_fromUtf8(""))
        self.t1GMMapWidth.setObjectName(_fromUtf8("t1GMMapWidth"))
        self.label_10 = QtGui.QLabel(self.t1GoogleMaps)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 31, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.t1GMMapHeight = QtGui.QLineEdit(self.t1GoogleMaps)
        self.t1GMMapHeight.setGeometry(QtCore.QRect(60, 170, 31, 20))
        self.t1GMMapHeight.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1GMMapHeight.setText(_fromUtf8(""))
        self.t1GMMapHeight.setObjectName(_fromUtf8("t1GMMapHeight"))
        self.label_11 = QtGui.QLabel(self.t1GoogleMaps)
        self.label_11.setGeometry(QtCore.QRect(40, 170, 16, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.t1Data.addTab(self.t1GoogleMaps, _fromUtf8(""))
        self.t1DataFrame = QtGui.QWidget()
        self.t1DataFrame.setObjectName(_fromUtf8("t1DataFrame"))
        self.t1DataFrameView = QtGui.QTableWidget(self.t1DataFrame)
        self.t1DataFrameView.setEnabled(True)
        self.t1DataFrameView.setGeometry(QtCore.QRect(0, 0, 941, 551))
        self.t1DataFrameView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1DataFrameView.setAlternatingRowColors(False)
        self.t1DataFrameView.setRowCount(10)
        self.t1DataFrameView.setColumnCount(3)
        self.t1DataFrameView.setObjectName(_fromUtf8("t1DataFrameView"))
        self.t1Data.addTab(self.t1DataFrame, _fromUtf8(""))
        self.t1Polygon1 = QtGui.QWidget()
        self.t1Polygon1.setObjectName(_fromUtf8("t1Polygon1"))
        self.t1Polygon1View = QtGui.QTableWidget(self.t1Polygon1)
        self.t1Polygon1View.setGeometry(QtCore.QRect(0, 0, 941, 551))
        self.t1Polygon1View.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1Polygon1View.setRowCount(10)
        self.t1Polygon1View.setColumnCount(2)
        self.t1Polygon1View.setObjectName(_fromUtf8("t1Polygon1View"))
        self.t1Data.addTab(self.t1Polygon1, _fromUtf8(""))
        self.t1Polygon2 = QtGui.QWidget()
        self.t1Polygon2.setEnabled(False)
        self.t1Polygon2.setObjectName(_fromUtf8("t1Polygon2"))
        self.t1Polygon2View = QtGui.QTableWidget(self.t1Polygon2)
        self.t1Polygon2View.setEnabled(False)
        self.t1Polygon2View.setGeometry(QtCore.QRect(0, 0, 941, 551))
        self.t1Polygon2View.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1Polygon2View.setRowCount(10)
        self.t1Polygon2View.setColumnCount(2)
        self.t1Polygon2View.setObjectName(_fromUtf8("t1Polygon2View"))
        self.t1Data.addTab(self.t1Polygon2, _fromUtf8(""))
        self.t1GoogleMaps2 = QtGui.QWidget()
        self.t1GoogleMaps2.setObjectName(_fromUtf8("t1GoogleMaps2"))
        self.t1GoogleMaps2View = QtWebKit.QWebView(self.t1GoogleMaps2)
        self.t1GoogleMaps2View.setGeometry(QtCore.QRect(100, 20, 843, 526))
        self.t1GoogleMaps2View.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.t1GoogleMaps2View.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.t1GoogleMaps2View.setObjectName(_fromUtf8("t1GoogleMaps2View"))
        self.t1GoogleMaps2Hint = QtGui.QLabel(self.t1GoogleMaps2)
        self.t1GoogleMaps2Hint.setGeometry(QtCore.QRect(0, 0, 947, 20))
        self.t1GoogleMaps2Hint.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);"))
        self.t1GoogleMaps2Hint.setText(_fromUtf8(""))
        self.t1GoogleMaps2Hint.setObjectName(_fromUtf8("t1GoogleMaps2Hint"))
        self.t1GM2maptype = QtGui.QRadioButton(self.t1GoogleMaps2)
        self.t1GM2maptype.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.t1GM2maptype.setChecked(True)
        self.t1GM2maptype.setAutoExclusive(True)
        self.t1GM2maptype.setObjectName(_fromUtf8("t1GM2maptype"))
        self.t1GM2maptype_2 = QtGui.QRadioButton(self.t1GoogleMaps2)
        self.t1GM2maptype_2.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.t1GM2maptype_2.setObjectName(_fromUtf8("t1GM2maptype_2"))
        self.t1GM2maptype_3 = QtGui.QRadioButton(self.t1GoogleMaps2)
        self.t1GM2maptype_3.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.t1GM2maptype_3.setObjectName(_fromUtf8("t1GM2maptype_3"))
        self.t1GM2maptype_4 = QtGui.QRadioButton(self.t1GoogleMaps2)
        self.t1GM2maptype_4.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.t1GM2maptype_4.setObjectName(_fromUtf8("t1GM2maptype_4"))
        self.t1GM2MapWidth = QtGui.QLineEdit(self.t1GoogleMaps2)
        self.t1GM2MapWidth.setGeometry(QtCore.QRect(10, 180, 31, 20))
        self.t1GM2MapWidth.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1GM2MapWidth.setText(_fromUtf8(""))
        self.t1GM2MapWidth.setObjectName(_fromUtf8("t1GM2MapWidth"))
        self.t1GM2MapHeight = QtGui.QLineEdit(self.t1GoogleMaps2)
        self.t1GM2MapHeight.setGeometry(QtCore.QRect(60, 180, 31, 20))
        self.t1GM2MapHeight.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1GM2MapHeight.setText(_fromUtf8(""))
        self.t1GM2MapHeight.setObjectName(_fromUtf8("t1GM2MapHeight"))
        self.label_6 = QtGui.QLabel(self.t1GoogleMaps2)
        self.label_6.setGeometry(QtCore.QRect(40, 180, 16, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.t1GoogleMaps2)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 31, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.t1GoogleMaps2)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.t1Data.addTab(self.t1GoogleMaps2, _fromUtf8(""))
        self.t1Map1 = QtGui.QWidget()
        self.t1Map1.setObjectName(_fromUtf8("t1Map1"))
        self.t1Map1View = QtGui.QGraphicsView(self.t1Map1)
        self.t1Map1View.setGeometry(QtCore.QRect(0, 0, 951, 551))
        self.t1Map1View.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1Map1View.setObjectName(_fromUtf8("t1Map1View"))
        self.t1Data.addTab(self.t1Map1, _fromUtf8(""))
        self.t1Map2 = QtGui.QWidget()
        self.t1Map2.setObjectName(_fromUtf8("t1Map2"))
        self.t1Map2View = QtGui.QGraphicsView(self.t1Map2)
        self.t1Map2View.setGeometry(QtCore.QRect(0, 0, 951, 551))
        self.t1Map2View.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.t1Map2View.setObjectName(_fromUtf8("t1Map2View"))
        self.t1Data.addTab(self.t1Map2, _fromUtf8(""))
        self.mainDataDisplay.addTab(self.tab_1, _fromUtf8(""))
        Locomotif.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Locomotif)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        Locomotif.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Locomotif)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Locomotif.setStatusBar(self.statusbar)
        self.QuickCommand = QtGui.QDockWidget(Locomotif)
        self.QuickCommand.setMinimumSize(QtCore.QSize(120, 168))
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
        self.cmdNewTab = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdNewTab.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdNewTab.setObjectName(_fromUtf8("cmdNewTab"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.cmdNewTab)
        self.QuickCommand.setWidget(self.dockWidgetContents)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickCommand)
        self.QuickStatus = QtGui.QDockWidget(Locomotif)
        self.QuickStatus.setMinimumSize(QtCore.QSize(120, 38))
        self.QuickStatus.setMaximumSize(QtCore.QSize(524287, 400))
        self.QuickStatus.setAutoFillBackground(False)
        self.QuickStatus.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QuickStatus.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickStatus.setObjectName(_fromUtf8("QuickStatus"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.cmdReadCSV = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdReadCSV.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.cmdReadCSV.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdReadCSV.setObjectName(_fromUtf8("cmdReadCSV"))
        self.cmdCreateVPolygone = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdCreateVPolygone.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.cmdCreateVPolygone.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdCreateVPolygone.setObjectName(_fromUtf8("cmdCreateVPolygone"))
        self.cmdCreateMaps = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdCreateMaps.setGeometry(QtCore.QRect(10, 130, 111, 23))
        self.cmdCreateMaps.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdCreateMaps.setObjectName(_fromUtf8("cmdCreateMaps"))
        self.cmdMapWidth = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.cmdMapWidth.setGeometry(QtCore.QRect(10, 100, 31, 20))
        self.cmdMapWidth.setObjectName(_fromUtf8("cmdMapWidth"))
        self.cmdMapHeight = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.cmdMapHeight.setGeometry(QtCore.QRect(70, 100, 31, 20))
        self.cmdMapHeight.setObjectName(_fromUtf8("cmdMapHeight"))
        self.cmdCreateDPolygone = QtGui.QPushButton(self.dockWidgetContents_2)
        self.cmdCreateDPolygone.setGeometry(QtCore.QRect(10, 70, 111, 23))
        self.cmdCreateDPolygone.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.cmdCreateDPolygone.setObjectName(_fromUtf8("cmdCreateDPolygone"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(50, 100, 16, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.QuickStatus.setWidget(self.dockWidgetContents_2)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickStatus)
        self.QuickTest = QtGui.QDockWidget(Locomotif)
        self.QuickTest.setObjectName(_fromUtf8("QuickTest"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.cmdDebug = QtGui.QPushButton(self.dockWidgetContents_3)
        self.cmdDebug.setGeometry(QtCore.QRect(10, 10, 102, 23))
        self.cmdDebug.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 255);"))
        self.cmdDebug.setObjectName(_fromUtf8("cmdDebug"))
        self.QuickTest.setWidget(self.dockWidgetContents_3)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickTest)
        self.actionQuit = QtGui.QAction(Locomotif)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionLoadGPSFile = QtGui.QAction(Locomotif)
        self.actionLoadGPSFile.setObjectName(_fromUtf8("actionLoadGPSFile"))
        self.actionLoadProject = QtGui.QAction(Locomotif)
        self.actionLoadProject.setObjectName(_fromUtf8("actionLoadProject"))
        self.actionHilfe = QtGui.QAction(Locomotif)
        self.actionHilfe.setObjectName(_fromUtf8("actionHilfe"))
        self.actionEinstellungen = QtGui.QAction(Locomotif)
        self.actionEinstellungen.setObjectName(_fromUtf8("actionEinstellungen"))
        self.actionInfo = QtGui.QAction(Locomotif)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionEdit = QtGui.QAction(Locomotif)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionCommands = QtGui.QAction(Locomotif)
        self.actionCommands.setObjectName(_fromUtf8("actionCommands"))
        self.actionLoadDataFile = QtGui.QAction(Locomotif)
        self.actionLoadDataFile.setObjectName(_fromUtf8("actionLoadDataFile"))
        self.menuFile.addAction(self.actionLoadDataFile)
        self.menuFile.addAction(self.actionLoadGPSFile)
        self.menuFile.addAction(self.actionLoadProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionCommands)
        self.menuView.addAction(self.actionEdit)
        self.menu.addAction(self.actionHilfe)
        self.menu.addSeparator()
        self.menu.addAction(self.actionEinstellungen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Locomotif)
        self.mainDataDisplay.setCurrentIndex(0)
        self.t1Data.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Locomotif.close)
        QtCore.QObject.connect(self.actionCommands, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickCommand.show)
        QtCore.QObject.connect(self.actionEdit, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickStatus.show)
        QtCore.QObject.connect(self.actionLoadProject, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openProjectFile)
        QtCore.QObject.connect(self.cmdLoadGPSFile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openGPSFile)
        QtCore.QObject.connect(self.cmdLoadProject, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openProjectFile)
        QtCore.QObject.connect(self.actionLoadGPSFile, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openGPSFile)
        QtCore.QObject.connect(self.cmdLoadDataFile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openDataFile)
        QtCore.QObject.connect(self.cmdCreateMaps, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doCreateMaps)
        QtCore.QObject.connect(self.cmdReadCSV, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doReadCSV)
        QtCore.QObject.connect(self.cmdCreateVPolygone, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doCreateVPolygone)
        QtCore.QObject.connect(self.cmdCreateDPolygone, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doCreateDPolygone)
        QtCore.QObject.connect(self.actionLoadDataFile, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openDataFile)
        QtCore.QObject.connect(self.actionEinstellungen, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.doConfigDialog)
        QtCore.QObject.connect(self.cmdDebug, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doDebugToConsole)
        QtCore.QObject.connect(self.t1GMmaptype, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGMMaptype1)
        QtCore.QObject.connect(self.t1GMmaptype_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGMMaptype2)
        QtCore.QObject.connect(self.t1GMmaptype_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGMMaptype3)
        QtCore.QObject.connect(self.t1GMmaptype_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGMMaptype4)
        QtCore.QObject.connect(self.t1GM2maptype, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGM2Maptype1)
        QtCore.QObject.connect(self.t1GM2maptype_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGM2Maptype2)
        QtCore.QObject.connect(self.t1GM2maptype_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGM2Maptype3)
        QtCore.QObject.connect(self.t1GM2maptype_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doSelectGM2Maptype4)
        QtCore.QObject.connect(self.mainDataDisplay, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), Locomotif.doMainTabSelect)
        QtCore.QObject.connect(self.mainDataDisplay, QtCore.SIGNAL(_fromUtf8("tabCloseRequested(int)")), Locomotif.doMainTabClose)
        QtCore.QObject.connect(self.cmdNewTab, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.doMainTabAdd)
        QtCore.QMetaObject.connectSlotsByName(Locomotif)

    def retranslateUi(self, Locomotif):
        Locomotif.setWindowTitle(_translate("Locomotif", "LocomotifGUI", None))
        self.label_2.setText(_translate("Locomotif", "Data File:", None))
        self.label_3.setText(_translate("Locomotif", "Data Sets:", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1FileData), _translate("Locomotif", "Data File", None))
        self.t1GMmaptype.setText(_translate("Locomotif", "hybrid", None))
        self.t1GMmaptype_2.setText(_translate("Locomotif", "satellite", None))
        self.t1GMmaptype_3.setText(_translate("Locomotif", "roadmap", None))
        self.t1GMmaptype_4.setText(_translate("Locomotif", "terrain", None))
        self.label_9.setText(_translate("Locomotif", "Maptype", None))
        self.label_10.setText(_translate("Locomotif", "Size", None))
        self.label_11.setText(_translate("Locomotif", "x", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1GoogleMaps), _translate("Locomotif", "Google Map", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1DataFrame), _translate("Locomotif", "Loaded Data Sets", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1Polygon1), _translate("Locomotif", "V-Polygon1", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1Polygon2), _translate("Locomotif", "V-Polygon2", None))
        self.t1GM2maptype.setText(_translate("Locomotif", "hybrid", None))
        self.t1GM2maptype_2.setText(_translate("Locomotif", "satellite", None))
        self.t1GM2maptype_3.setText(_translate("Locomotif", "roadmap", None))
        self.t1GM2maptype_4.setText(_translate("Locomotif", "terrain", None))
        self.label_6.setText(_translate("Locomotif", "x", None))
        self.label_7.setText(_translate("Locomotif", "Size", None))
        self.label_8.setText(_translate("Locomotif", "Maptype", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1GoogleMaps2), _translate("Locomotif", "Google Map", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1Map1), _translate("Locomotif", "Map1", None))
        self.t1Data.setTabText(self.t1Data.indexOf(self.t1Map2), _translate("Locomotif", "Map2", None))
        self.mainDataDisplay.setTabText(self.mainDataDisplay.indexOf(self.tab_1), _translate("Locomotif", "Data Record  1", None))
        self.menuFile.setTitle(_translate("Locomotif", "File", None))
        self.menuView.setTitle(_translate("Locomotif", "Edit", None))
        self.menu.setTitle(_translate("Locomotif", "?", None))
        self.QuickCommand.setWhatsThis(_translate("Locomotif", "<html><head/><body><p>Bla Bla ...</p></body></html>", None))
        self.QuickCommand.setWindowTitle(_translate("Locomotif", "Commands", None))
        self.cmdLoadDataFile.setText(_translate("Locomotif", "Select Data File", None))
        self.cmdLoadGPSFile.setText(_translate("Locomotif", "Select GPS File", None))
        self.cmdLoadProject.setText(_translate("Locomotif", "Select Project", None))
        self.cmdNewTab.setText(_translate("Locomotif", "New Data Tab", None))
        self.QuickStatus.setWindowTitle(_translate("Locomotif", "Working Steps", None))
        self.cmdReadCSV.setText(_translate("Locomotif", "Create Data Frames", None))
        self.cmdCreateVPolygone.setText(_translate("Locomotif", "Calculate V Polynoms", None))
        self.cmdCreateMaps.setText(_translate("Locomotif", "Create Maps", None))
        self.cmdCreateDPolygone.setText(_translate("Locomotif", "Calculate D Polynoms", None))
        self.label_5.setText(_translate("Locomotif", "x", None))
        self.QuickTest.setWindowTitle(_translate("Locomotif", "Testfunktionen", None))
        self.cmdDebug.setText(_translate("Locomotif", "DEBUG", None))
        self.actionQuit.setText(_translate("Locomotif", "Quit", None))
        self.actionLoadGPSFile.setText(_translate("Locomotif", "Open GPS File...", None))
        self.actionLoadProject.setText(_translate("Locomotif", "Open Project...", None))
        self.actionHilfe.setText(_translate("Locomotif", "Help", None))
        self.actionEinstellungen.setText(_translate("Locomotif", "Settings...", None))
        self.actionInfo.setText(_translate("Locomotif", "Info...", None))
        self.actionEdit.setText(_translate("Locomotif", "Current Data Set", None))
        self.actionCommands.setText(_translate("Locomotif", "Quick Command Box", None))
        self.actionLoadDataFile.setText(_translate("Locomotif", "Open Data File...", None))

from PyQt4 import QtWebKit
