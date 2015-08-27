# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Mirko
"""
import sys
import os
from PyQt4 import QtGui, QtCore
from ui.Ui_Locomotif import Ui_Locomotif
from tools.Tools_Locomotif import Tools_Locomotif
from work.Work_Locomotif import Work_Locomotif
from config.Config_Configuration import *
from ConfigDialog import ConfigDialog
from data.Rundata_Locomotif import Rundata_Locomotif
from data.Rundata_Locomotif import g_rundata
from data.Rundata_Widgets import g_tabwidgets
from uicustom.UiTools import *
import locomotif as loc

# globaler Datenspeicher
uiTools = UiTools()
selectedRundata = None

class Locomotif(QtGui.QMainWindow):
	"""
	Docstring
	"""
	def __init__(self, parent=None):
		"""
		Docstring
		"""
		# load all basic PyQt4 functions from QWidget
		QtGui.QWidget.__init__(self, parent)
        
		# load the ui
		self.ui = Ui_Locomotif()
		self.ui.setupUi(self)
		
		# setup global config
		configData.setupConfig()

		# load tools
		self.tools = Tools_Locomotif()
		self.tools.setupTools()
		# load work
		self.work = Work_Locomotif()
		self.work.setupWork()
        
		# load configuration values and store in config class
		__base__ = os.path.abspath(os.path.dirname(__file__))
		configData.initConfig( __base__ )
		configData.debugConfig()

		# setup global rundata buffer (not sure whetter this is required any longer)
		g_rundata.setupRundata()
		g_rundata.setDataFont( configData.getDataFont() )
		
		# initial values for maps in the working dock widget
		mapWidth = configData.getMapWidth()
		g_rundata.setMapWidth( mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = configData.getMapHeight()
		g_rundata.setMapHeight( mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))

		# setup/select the main data display
		mainDataWidget = self.ui.mainDataDisplay
		# delete the first tab page that is created by the code
		# from the QT-Designer
		mainDataWidget.removeTab(0)

		# setup customized main tab page
		uiTools.setupUiTools(self)
		uiTools.initCustomTabWidget(self.ui.mainDataDisplay, 0 )
		# and now add the first custom tab page
		uiTools.addCustomTabPage()
		uiTools.selectCustomTabPage(0)
		
		# initial values for google maps in custom tab page
		mapWidth = configData.getGoogleMapWidth()
		g_rundata.setGoogleMapWidth( mapWidth )
		#g_tabwidgets.t1GMMapWidth.setText(str(mapWidth))
		#g_tabwidgets.t1GM2MapWidth.setText(str(mapWidth))
		mapHeight = configData.getGoogleMapHeight()
		g_rundata.setGoogleMapHeight( mapHeight )
		#g_tabwidgets.t1GMMapHeight.setText(str(mapWidth))
		#g_tabwidgets.t1GM2MapHeight.setText(str(mapWidth))
		
# These are custom slots used within Qt Designer

	def doConfigDialog(self, Locomotif):
		print "open configuration dialog"
		dialog = ConfigDialog(self)
		dialog.setModal(1)
		ret = dialog.exec_()
		
		# transfer (new) map sizes
		mapWidth = configData.getMapWidth()
		g_rundata.setMapWidth( mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = configData.getMapHeight()
		g_rundata.setMapHeight( mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))
		
		# transfer (new) google maps settings
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
		# following values must fit to combobox in configuration
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
		# following values must fit to combobox in configuration
		if maptype == "hybrid":
			g_tabwidgets.t1GM2maptype.setChecked(True)
		if maptype == "satellite":
			g_tabwidgets.t1GM2maptype_2.setChecked(True)
		if maptype == "roadmap":
			g_tabwidgets.t1GM2maptype_3.setChecked(True)
		if maptype == "terrain":
			g_tabwidgets.t1GM2maptype_4.setChecked(True)
		
	def openDataFile(self, Locomotif):
		""" Load a Data File for Further Processing """
		dataFilename = self.tools.selectDataFile()
		if dataFilename == "":
			self.tools.showInfo( "Info", "NO FILE SELECTED" )
			return 0
		
		# deactivate all tabs 
		self.work.workCleanTabs( g_tabwidgets, g_rundata, 0 )
		g_tabwidgets.t1Data.setCurrentIndex(0)
		
		# store name in global data	
		g_rundata.setDataFileName( dataFilename )
		# set data into current tab
		g_tabwidgets.t1LoadedDataFilename.setText(dataFilename)
		# load and display initial data
		self.work.readDataFileIntoTable( g_tabwidgets, dataFilename )
		self.work.markDataOnGoogleMap( g_tabwidgets, g_rundata )
		print "data marked on google map type " + g_rundata.getGoogle1Maptype()
		
		# initial names for maps
		mapv1Filename = configData.getMapPath() + "/map1_v.png"
		mapv2Filename = configData.getMapPath() + "/map2_v.png"
		g_rundata.setV1Mapname( mapv1Filename )
		g_rundata.setV2Mapname( mapv2Filename )
		mapd1Filename = configData.getMapPath() + "/map1_d.png"
		mapd2Filename = configData.getMapPath() + "/map2_d.png"
		g_rundata.setD1Mapname( mapd1Filename )
		g_rundata.setD2Mapname( mapd2Filename )
		
		return 1
		
	def doMainTabAdd(self, Locomotif ):
		uiTools.addCustomTabPage()

	def doMainTabSelect(self, currentIndex):
		print "maintabselect " + str(currentIndex)
		if currentIndex<0:
			return
		print "do maintabselect " + str(currentIndex)
		uiTools.selectCustomTabPage(currentIndex)

	def doMainTabClose(self, currentIndex):
		print "maintabclose " + str(currentIndex)
		uiTools.removeCustomTabPage(currentIndex)

	def openGPSFile(self, Locomotif):
		""" Load a GPS File for Further Processing """
		gpsFileName = self.tools.selectGPSFile()

	def openProjectFile(self, Locomotif):
		""" Load a Project File for Further Processing """
		projectFileName = self.tools.selectProjectFile()

	def doSelectGMMaptype1(self, Locomotif):
		g_rundata.setGoogle1Maptype("hybrid");
		self.work.markDataOnGoogleMap( g_tabwidgets, g_rundata )

	def doSelectGMMaptype2(self, Locomotif):
		g_rundata.setGoogle1Maptype("satellite");
		self.work.markDataOnGoogleMap( g_tabwidgets, g_rundata )

	def doSelectGMMaptype3(self, Locomotif):
		g_rundata.setGoogle1Maptype("roadmap");
		self.work.markDataOnGoogleMap( g_tabwidgets, g_rundata )

	def doSelectGMMaptype4(self, Locomotif):
		g_rundata.setGoogle1Maptype("terrain");
		self.work.markDataOnGoogleMap( g_tabwidgets, g_rundata )

	def doReadCSV(self, Locomotif):
		"""
		Reload the CSV DataFrames with the given name
		"""
		self.work.workReadCSV( g_tabwidgets, g_rundata )
		df = g_rundata.getDF()
		self.work.putCSVIntoTable( g_tabwidgets, df )
		"""
		Create Cluster for the loaded Dataframe
		"""
		self.work.workCreateCluster( g_tabwidgets, g_rundata )

	def doCreateVPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		print "CREATE POLYNOME"
		self.work.workCreateVPolygone(g_tabwidgets, g_rundata )
		print "CREATE MAP"
		self.work.markPolygonOnGoogleMap(g_tabwidgets, g_rundata, g_rundata.getVoronoi1() )

	def doCreateDPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateDPolygone(g_tabwidgets, g_rundata )
		self.work.markPolygonOnGoogleMap(g_tabwidgets, g_rundata, g_rundata.getDelaunay1() )

	def doSelectGM2Maptype1(self, Locomotif):
		g_rundata.setGoogle2Maptype("hybrid");
		self.work.refreshPolygonOnGoogleMap( g_tabwidgets, g_rundata )

	def doSelectGM2Maptype2(self, Locomotif):
		g_rundata.setGoogle2Maptype("satellite");
		self.work.refreshPolygonOnGoogleMap( g_tabwidgets, g_rundata )

	def doSelectGM2Maptype3(self, Locomotif):
		g_rundata.setGoogle2Maptype("roadmap");
		self.work.refreshPolygonOnGoogleMap( g_tabwidgets, g_rundata )

	def doSelectGM2Maptype4(self, Locomotif):
		g_rundata.setGoogle2Maptype("terrain");
		self.work.refreshPolygonOnGoogleMap( g_tabwidgets, g_rundata )

	def doCreateMaps(self, Locomotif):
		"""
		Slot for button CreateMap
		"""
		self.work.workCreateMaps( self, g_tabwidgets, g_rundata )

	def doDebugToConsole(self, Locomotif):
		configData.debugConfig()
		g_rundata.debugRundata("g_rundata")
		uiTools.debugUiTools()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Locomotif()
    myapp.show()
    sys.exit(app.exec_())