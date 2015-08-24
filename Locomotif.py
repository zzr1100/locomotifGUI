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
from data.Rundata_Locomotif import Rundata_Locomotif
from config.Config_Configuration import *
from ConfigDialog import ConfigDialog
import locomotif as loc

# globaler Datenspeicher
rundata = Rundata_Locomotif()

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
		# setup global rundata
		rundata.setupRundata()
		# load work
		self.work = Work_Locomotif()
		self.work.setupWork(self)
        
		# create font for data display
		dataFont = QtGui.QFont()
		dataFont.setStyleHint(QtGui.QFont.Courier)
		rundata.setDataFont( dataFont )
		
		# more initialisations
		self.ui.mainDataDisplay.setTabText(0,"Data Record 1")
		self.ui.mainDataDisplay.setTabText(1,"Data Record 2")
		self.ui.mainDataDisplay.setCurrentIndex(0)
		
		# load configuration values and stor in config class
		__base__ = os.path.abspath(os.path.dirname(__file__))
		configData.initConfig( __base__ )
		configData.debugConfig()

		# initial values for maps
		mapWidth = configData.getMapWidth()
		rundata.setMapWidth( mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = configData.getMapHeight()
		rundata.setMapHeight( mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))

		# initial values for google maps
		mapWidth = configData.getGoogleMapWidth()
		rundata.setGoogleMapWidth( mapWidth )
		self.ui.t1GMMapWidth.setText(str(mapWidth))
		self.ui.t1GM2MapWidth.setText(str(mapWidth))
		mapHeight = configData.getGoogleMapHeight()
		rundata.setGoogleMapHeight( mapHeight )
		self.ui.t1GMMapHeight.setText(str(mapWidth))
		self.ui.t1GM2MapHeight.setText(str(mapWidth))
		
# These are custom slots used within Qt Designer

	def doDebugToConsole(self, Locomotif):
		configData.debugConfig()
		rundata.debugRundata()

	def doConfigDialog(self, Locomotif):
		print "open configuration dialog"
		dialog = ConfigDialog(self)
		dialog.setModal(1)
		ret = dialog.exec_()
		
		# transfer (new) map sizes
		mapWidth = configData.getMapWidth()
		rundata.setMapWidth( mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = configData.getMapHeight()
		rundata.setMapHeight( mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))
		
		# transfer (new) google maps settings
		mapWidth = configData.getGoogleMapWidth()
		rundata.setGoogleMapWidth( mapWidth )
		self.ui.t1GMMapWidth.setText(str(mapWidth))
		self.ui.t1GM2MapWidth.setText(str(mapWidth))
		mapHeight = configData.getGoogleMapHeight()
		rundata.setGoogleMapHeight( mapHeight )
		self.ui.t1GMMapHeight.setText(str(mapHeight))
		self.ui.t1GM2MapHeight.setText(str(mapHeight))
		
		maptype = configData.getGoogle1Maptype()
		rundata.setGoogle1Maptype( maptype )
		# followinfg values must fit to combobox in configuration
		if maptype == "hybrid":
			self.ui.t1GMmaptype.setChecked(True)
		if maptype == "satellite":
			self.ui.t1GMmaptype_2.setChecked(True)
		if maptype == "roadmap":
			self.ui.t1GMmaptype_3.setChecked(True)
		if maptype == "terrain":
			self.ui.t1GMmaptype_4.setChecked(True)
		
		maptype = configData.getGoogle2Maptype()
		rundata.setGoogle2Maptype( maptype )
		self.ui.t1GM2maptype_2.setChecked(True)
		# followinfg values must fit to combobox in configuration
		if maptype == "hybrid":
			self.ui.t1GM2maptype.setChecked(True)
		if maptype == "satellite":
			self.ui.t1GM2maptype_2.setChecked(True)
		if maptype == "roadmap":
			self.ui.t1GM2maptype_3.setChecked(True)
		if maptype == "terrain":
			self.ui.t1GM2maptype_4.setChecked(True)
		
	def openDataFile(self, Locomotif):
		""" Load a Data File for Further Processing """
		dataFilename = self.tools.selectDataFile()
		if dataFilename == "":
			self.tools.showInfo( "Info", "NO FILE SELECTED" )
			return 0
		
		# deactivate all tabs 
		self.work.workCleanTabs( self, rundata, 0 )
		self.ui.t1Data.setCurrentIndex(0)
		
		# store nme in global data	
		rundata.setDataFileName( dataFilename )
		self.ui.loadedDataFilename.setText(dataFilename)
		self.ui.t1LoadedDataFilename.setText(dataFilename)
		# load and display initial data
		self.work.readDataFileIntoTable( self, dataFilename )
		self.work.markDataOnGoogleMap( self, rundata )
		print "data marked on google map type " + rundata.getGoogle1Maptype()
		
		# initial names for maps
		mapv1Filename = configData.getMapPath() + "/map1_v.png"
		mapv2Filename = configData.getMapPath() + "/map2_v.png"
		rundata.setV1Mapname( mapv1Filename )
		rundata.setV2Mapname( mapv2Filename )
		mapd1Filename = configData.getMapPath() + "/map1_d.png"
		mapd2Filename = configData.getMapPath() + "/map2_d.png"
		rundata.setD1Mapname( mapd1Filename )
		rundata.setD2Mapname( mapd2Filename )
		
		return 1
		
	def openGPSFile(self, Locomotif):
		""" Load a GPS File for Further Processing """
		gpsFileName = self.tools.selectGPSFile()

	def openProjectFile(self, Locomotif):
		""" Load a Project File for Further Processing """
		projectFileName = self.tools.selectProjectFile()

	def doSelectGMMaptype1(self, Locomotif):
		rundata.setGoogle1Maptype("hybrid");
		self.work.markDataOnGoogleMap( self, rundata )

	def doSelectGMMaptype2(self, Locomotif):
		rundata.setGoogle1Maptype("satellite");
		self.work.markDataOnGoogleMap( self, rundata )

	def doSelectGMMaptype3(self, Locomotif):
		rundata.setGoogle1Maptype("roadmap");
		self.work.markDataOnGoogleMap( self, rundata )

	def doSelectGMMaptype4(self, Locomotif):
		rundata.setGoogle1Maptype("terrain");
		self.work.markDataOnGoogleMap( self, rundata )

	def doReadCSV(self, Locomotif):
		"""
		Reload the CSV DataFrames with the given name
		"""
		self.work.workReadCSV( self, rundata )
		df = rundata.getDF()
		self.work.putCSVIntoTable( self, df )
		"""
		Create Cluster for the loaded Dataframe
		"""
		self.work.workCreateCluster( self, rundata )

	def doCreateVPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateVPolygone(self, rundata )
		self.work.markPolygonOnGoogleMap(self, rundata, rundata.getVoronoi1() )

	def doCreateDPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateDPolygone(self, rundata )
		self.work.markPolygonOnGoogleMap(self, rundata, rundata.getDelaunay1() )

	def doSelectGM2Maptype1(self, Locomotif):
		rundata.setGoogle2Maptype("hybrid");
		self.work.refreshPolygonOnGoogleMap( self, rundata )

	def doSelectGM2Maptype2(self, Locomotif):
		rundata.setGoogle2Maptype("satellite");
		self.work.refreshPolygonOnGoogleMap( self, rundata )

	def doSelectGM2Maptype3(self, Locomotif):
		rundata.setGoogle2Maptype("roadmap");
		self.work.refreshPolygonOnGoogleMap( self, rundata )

	def doSelectGM2Maptype4(self, Locomotif):
		rundata.setGoogle2Maptype("terrain");
		self.work.refreshPolygonOnGoogleMap( self, rundata )

	def doCreateMaps(self, Locomotif):
		"""
		Slot for button CreateMap
		"""
		self.work.workCreateMaps( self, rundata )

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Locomotif()
    myapp.show()
    sys.exit(app.exec_())