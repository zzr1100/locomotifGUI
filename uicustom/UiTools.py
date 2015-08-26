# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""

import sys
from PyQt4 import QtCore, QtGui, QtWebKit
from config.Config_Configuration import *
from data.Rundata_Locomotif import Rundata_Locomotif
from data.Rundata_Locomotif import g_rundata
from data.Rundata_Widgets import Rundata_TabWidgets
from data.Rundata_Widgets import g_tabwidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class UiTools(object):

	def setupUiTools(self,locapp):
		self.locapp = locapp
		self.tabWidget = None
		self.tabList = []
		self.numTabs = 0
		self.lastTabIndex = 0
		self.nextinternalnum = -1
		self.selectedIndex = -1
		self.selectedInternalnum = -1
		self.selectedCustomTab = None
		self.selectedRundata = None

	def debugUiTools(self):
		print "---------------------------------"
		print "Custom Main tab Handling"
		print "---------------------------------"
		print "numTabs = " + str(self.numTabs)
		print "lastTabIndex = " + str(self.lastTabIndex)
		print "nextinternalnum = " + str(self.nextinternalnum)
		print "selectedIndex = " + str(self.selectedIndex)
		print "selectedInternalnum = " + str(self.selectedInternalnum)
		print "selectedCustomTab = " + str(self.selectedCustomTab)
		self.selectedCustomTab.debugTabElement()
		print "selectedRundata = " + str(self.selectedRundata)
		self.selectedRundata.debugRundata()
		print "---------------------------------"
		print "list of "+str(len(self.tabList))+"custom tab elements = " + str(self.tabList)
		for tabElem in self.tabList:
			tabElem.debugTabElement()

	def initCustomTabWidgetTEST(self, tabWidget, numTabs ):
		self.tabWidget = tabWidget
		# dummy tab and rundata at first position
		tab1 = UiCustomTab()
		tab1.initTabElement(self.locapp,0)
		self.tabList = [tab1]
		self.numTabs = numTabs
		self.lastTabIndex = numTabs -1
		self.selectedIndex = 0
		self.nextinternalnum = numTabs
		self.selectedCustomTab = tab1
		self.selectedInternalnum = 0
		self.selectedRundata = tab1.getRundataBuffer()
			
	def initCustomTabWidget(self, tabWidget, numTabs ):
		self.tabWidget = tabWidget
		self.tabList = []
		self.numTabs = 0
		self.lastTabIndex = -1
		self.selectedIndex = 0
		self.nextinternalnum = 0
		self.selectedCustomTab = None
		self.selectedInternalnum = 0
		self.selectedRundata = None

	def addCustomTabPage(self):
		print "add a custom tab page"
		newTabElem = UiCustomTab()
		newTabElem.initTabElement(self.locapp,self.nextinternalnum)
		newTabElemWidget = newTabElem.getTabElementWidget()
		# insert this new tab element into our custom tab widget
		self.tabWidget.addTab(newTabElemWidget, _fromUtf8(""))
		tabTitle = "Data Record " + str(self.nextinternalnum+1)
		self.tabWidget.setTabText(self.tabWidget.indexOf(newTabElemWidget), tabTitle )
		# adjust counter
		self.tabList.append( newTabElem )
		self.numTabs = self.numTabs + 1
		self.lastTabIndex = self.numTabs -1		
		self.nextinternalnum = self.nextinternalnum + 1

	def selectCustomTabPage(self, selectedIndex ):
		print "switch to custom tab page"
		# save the global rundata into the current tab element
		# before switching to another one
		if self.selectedRundata != None:
			self.selectedRundata.get_g_rundata()
		# now switch to another tab
		print "Select tab " + str(selectedIndex)
		self.selectedIndex = selectedIndex
		self.selectedCustomTab = self.tabList[selectedIndex]
		self.selectedInternalnum = self.selectedCustomTab.getInternalnum()
		self.selectedRundata = self.selectedCustomTab.getRundataBuffer()
		# set this widgets as the global widgets to work on it now
		self.selectedCustomTab.getWidgetBuffer().set_g_tabwidgets()
		# set this rundata as the global rundata to work on it now
		self.selectedRundata.set_g_rundata()
		# insert some start values into the widgets
		mapWidth = configData.getGoogleMapWidth()
		g_rundata.setGoogleMapWidth( mapWidth )
		g_tabwidgets.t1GMMapWidth.setText(str(mapWidth))
		g_tabwidgets.t1GM2MapWidth.setText(str(mapWidth))
		mapHeight = configData.getGoogleMapHeight()
		g_rundata.setGoogleMapHeight( mapHeight )
		g_tabwidgets.t1GMMapHeight.setText(str(mapHeight))
		g_tabwidgets.t1GM2MapHeight.setText(str(mapHeight))
		maptype = configData.getGoogle1Maptype()
		g_rundata.setGoogle1Maptype( maptype )
		if maptype == "hybrid":
			g_tabwidgets.t1GMmaptype.setChecked(True)
		if maptype == "satellite":
			g_tabwidgets.t1GMmaptype_2.setChecked(True)
		if maptype == "roadmap":
			g_tabwidgets.t1GMmaptype_3.setChecked(True)
		if maptype == "terrain":
			g_tabwidgets.t1GMmaptype_4.setChecked(True)
		maptype = configData.getGoogle2Maptype()
		g_rundata.setGoogle2Maptype( maptype )
		if maptype == "hybrid":
			g_tabwidgets.t1GM2maptype.setChecked(True)
		if maptype == "satellite":
			g_tabwidgets.t1GM2maptype_2.setChecked(True)
		if maptype == "roadmap":
			g_tabwidgets.t1GM2maptype_3.setChecked(True)
		if maptype == "terrain":
			g_tabwidgets.t1GM2maptype_4.setChecked(True)

	def removeCustomTabPage(self, selectedIndex ):
		if self.numTabs<=1:
			print "Last Tab cannot be closed"
			return
		print "Close tab " + str(selectedIndex)
		self.tabWidget.removeTab(selectedIndex)
		self.numTabs = self.numTabs - 1
		self.lastTabIndex = self.numTabs -1
		
	def getSelectedCustomTab(self):
		return self.selectedCustomTab

		
class UiCustomTab(object):
	"""
	This class creates a tab element and all fields included in it
	Supplies a rundata element for a users dataset
	"""

	def initTabElement(self,locapp,internalnum):
		self.internalnum = internalnum;
		
		# create ui widgets for this custom tab element and collect
		# them into a buffer
		self.widgets = Rundata_TabWidgets()
		self.widgets.init()
		# set title to the new tab widget
		
		# set slots and signals
		#QtCore.QObject.connect(self.t1GMmaptype, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGMMaptype1)
		#QtCore.QObject.connect(self.t1GMmaptype_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGMMaptype2)
		#QtCore.QObject.connect(self.t1GMmaptype_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGMMaptype3)
		#QtCore.QObject.connect(self.t1GMmaptype_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGMMaptype4)
		#QtCore.QObject.connect(self.t1GM2maptype, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGM2Maptype1)
		#QtCore.QObject.connect(self.t1GM2maptype_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGM2Maptype2)
		#QtCore.QObject.connect(self.t1GM2maptype_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGM2Maptype3)
		#QtCore.QObject.connect(self.t1GM2maptype_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), locapp.doSelectGM2Maptype4)
		# store the tab widget

		# create an application data buffer for this tab element
		rundata = Rundata_Locomotif()
		rundata.setupRundata()	
		# and init the rundata
		rundata.setDataFont( configData.getDataFont() )
		mapWidth = configData.getMapWidth()
		rundata.setMapWidth( mapWidth )
		mapHeight = configData.getMapHeight()
		rundata.setMapHeight( mapHeight )
		mapWidth = configData.getGoogleMapWidth()
		rundata.setGoogleMapWidth( mapWidth )
		mapHeight = configData.getGoogleMapHeight()
		rundata.setGoogleMapHeight( mapHeight )
		self.rundata = rundata
		
	def debugTabElement(self):
		print "self.internalnum = " + str(self.internalnum)
		print "self.tabElement = " + str(self.tabElement)
		print "self.t1LoadedDataFilename = " + str(self.t1LoadedDataFilename)
		print "self.t1LoadedDatasets = " + str(self.t1LoadedDatasets)
		print "self.t1DataFrame = " + str(self.t1DataFrame)
		print "self.t1DataFrameView = " + str(self.t1DataFrameView)
		print "self.rundata = " + str(self.rundata)

	def setInternalnum(self, internalnum):
		self.internalnum = internalnum
		
	def getInternalnum(self):
		return self.internalnum
		
	def getRundataBuffer(self):
		return self.rundata

	def getWidgetBuffer(self):
		return self.widgets
		
	# access the UI elements of this tab 
	def getTabElementWidget(self):
		return self.widgets.getTab()

	def gett1LoadedDataFilename(self):
		return self.widgets.t1LoadedDataFilename
		
	def gett1LoadedDatasets(self):
		return self.widgets.t1LoadedDatasets
	
	def gett1DataFrame(self):
		return self.widgets.t1DataFrame

	def gett1DataFrameView(self):
		return self.widgets.t1DataFrameView


		