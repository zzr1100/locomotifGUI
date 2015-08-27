# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""

import sys
from PyQt4 import QtCore, QtGui, QtWebKit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Rundata_TabWidgets(object):
	"""
	Rundata object that keeps ths list of ui widgets of one tab element
	of the main data display. 
	"""
	
	def init(self,resourcePath):
		newTabElement = QtGui.QWidget()
		newTabElement.setObjectName(_fromUtf8("newtab"))
		self.tabElement = newTabElement
		self.label_2 = QtGui.QLabel(newTabElement)
		self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 16))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.t1LoadedDataFilename = QtGui.QLineEdit(newTabElement)
		self.t1LoadedDataFilename.setGeometry(QtCore.QRect(80, 20, 531, 20))
		self.t1LoadedDataFilename.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
		self.t1LoadedDataFilename.setObjectName(_fromUtf8("t1LoadedDataFilename"))
		self.label_3 = QtGui.QLabel(newTabElement)
		self.label_3.setGeometry(QtCore.QRect(20, 50, 46, 13))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.t1LoadedDatasets = QtGui.QLineEdit(newTabElement)
		self.t1LoadedDatasets.setGeometry(QtCore.QRect(80, 50, 531, 20))
		self.t1LoadedDatasets.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
		self.t1LoadedDatasets.setObjectName(_fromUtf8("t1LoadedDatasets"))
		self.t1Data = QtGui.QTabWidget(newTabElement)
		self.t1Data.setGeometry(QtCore.QRect(20, 90, 951, 571))
		self.t1Data.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
		self.t1Data.setObjectName(_fromUtf8("t1Data"))
		self.t1FileData = QtGui.QWidget()
		self.t1FileData.setObjectName(_fromUtf8("t1FileData"))
		self.t1FileDataView = QtGui.QTableWidget(self.t1FileData)
		self.t1FileDataView.setGeometry(QtCore.QRect(0, 0, 941, 551))
		self.t1FileDataView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
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
		self.t1GoogleMapsHint.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);"))
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
		self.t1GoogleMaps2Hint.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);"))
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
		self.translate()
		# TEST: ADD ICONS TO TABS
		self.icon_data = QtGui.QIcon( resourcePath + "/icon_data.gif" )
		self.icon_google = QtGui.QIcon( resourcePath + "/icon_google.png" )
		self.icon_bio = QtGui.QIcon( resourcePath + "/icon_bio.png" )
		self.icon_ok = QtGui.QIcon( resourcePath + "/icon_ok.gif" )
		self.icon_disabled = QtGui.QIcon( resourcePath + "/icon_disabled.gif" )
		self.t1Data.setTabIcon( 0, self.icon_data )
		self.t1Data.setTabIcon( 1, self.icon_google )
		self.t1Data.setTabIcon( 2, self.icon_data )
		self.t1Data.setTabIcon( 3, self.icon_data )
		self.t1Data.setTabIcon( 4, self.icon_data )
		self.t1Data.setTabIcon( 5, self.icon_google )
		self.t1Data.setTabIcon( 6, self.icon_bio )
		self.t1Data.setTabIcon( 7, self.icon_bio )
		

	def translate(self):
		self.label_2.setText("Data File:")
		self.label_3.setText("Data Sets:")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1FileData), "Data File")
		self.t1GMmaptype.setText("hybrid")
		self.t1GMmaptype_2.setText("satellite")
		self.t1GMmaptype_3.setText("roadmap")
		self.t1GMmaptype_4.setText("terrain")
		self.label_9.setText("Maptype")
		self.label_10.setText("Size")
		self.label_11.setText("x")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1GoogleMaps), "Google Map")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1DataFrame), "Loaded Data Sets")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1Polygon1), "V-Polygon1")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1Polygon2), "V-Polygon2")
		self.t1GM2maptype.setText("hybrid")
		self.t1GM2maptype_2.setText("satellite")
		self.t1GM2maptype_3.setText("roadmap")
		self.t1GM2maptype_4.setText("terrain")
		self.label_6.setText("x")
		self.label_7.setText("Size")
		self.label_8.setText("Maptype")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1GoogleMaps2), "Google Map")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1Map1), "Map1")
		self.t1Data.setTabText(self.t1Data.indexOf(self.t1Map2), "Map2")
		
	def getTab(self):
		return self.tabElement
		
	def set_g_tabwidgets( self ):
		"""
		Copy content from given widgets buffer into g_tabwidgets
		"""
		g_tabwidgets.tabElement = self.tabElement
		g_tabwidgets.t1LoadedDataFilename = self.t1LoadedDataFilename
		g_tabwidgets.t1LoadedDatasets = self.t1LoadedDatasets
		g_tabwidgets.t1Data = self.t1Data
		g_tabwidgets.t1FileData = self.t1FileData
		g_tabwidgets.t1FileDataView = self.t1FileDataView
		g_tabwidgets.t1GoogleMaps = self.t1GoogleMaps
		g_tabwidgets.t1GoogleMapsView = self.t1GoogleMapsView
		g_tabwidgets.t1GoogleMapsHint = self.t1GoogleMapsHint
		g_tabwidgets.t1GMmaptype = self.t1GMmaptype
		g_tabwidgets.t1GMmaptype_2 = self.t1GMmaptype_2
		g_tabwidgets.t1GMmaptype_3 = self.t1GMmaptype_3
		g_tabwidgets.t1GMmaptype_4 = self.t1GMmaptype_4
		g_tabwidgets.t1GMMapWidth = self.t1GMMapWidth
		g_tabwidgets.t1GMMapHeight = self.t1GMMapHeight
		g_tabwidgets.t1DataFrame = self.t1DataFrame
		g_tabwidgets.t1DataFrameView = self.t1DataFrameView
		g_tabwidgets.t1Polygon1 = self.t1Polygon1
		g_tabwidgets.t1Polygon1View = self.t1Polygon1View
		g_tabwidgets.t1Polygon2 = self.t1Polygon2
		g_tabwidgets.t1Polygon2View = self.t1Polygon2View
		g_tabwidgets.t1GoogleMaps2 = self.t1GoogleMaps2
		g_tabwidgets.t1GoogleMaps2View = self.t1GoogleMaps2View
		g_tabwidgets.t1GoogleMaps2Hint = self.t1GoogleMaps2Hint
		g_tabwidgets.t1GM2maptype = self.t1GM2maptype
		g_tabwidgets.t1GM2maptype_2 = self.t1GM2maptype_2
		g_tabwidgets.t1GM2maptype_3 = self.t1GM2maptype_3
		g_tabwidgets.t1GM2maptype_4 = self.t1GM2maptype_4
		g_tabwidgets.t1GM2MapWidth = self.t1GM2MapWidth
		g_tabwidgets.t1GM2MapHeight = self.t1GM2MapHeight
		g_tabwidgets.t1Map1 = self.t1Map1
		g_tabwidgets.t1Map1View = self.t1Map1View
		g_tabwidgets.t1Map2 = self.t1Map2
		g_tabwidgets.t1Map2View = self.t1Map2View
		g_tabwidgets.icon_data = self.icon_data
		g_tabwidgets.icon_google = self.icon_google
		g_tabwidgets.icon_bio = self.icon_bio
		g_tabwidgets.icon_ok = self.icon_ok
		g_tabwidgets.icon_disabled = self.icon_disabled
		
# Global Rundata buffer to be used throughout the application
# The widgets from the selected tab is moved to this buffer
# "This buffer points to the selected widgets"
		
g_tabwidgets = Rundata_TabWidgets()

