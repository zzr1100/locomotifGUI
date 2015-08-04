# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Mirko
"""
import sys
from PyQt4 import QtGui, QtCore
from ui.Ui_Locomotif import Ui_Locomotif
from tools.Tools_Locomotif import Tools_Locomotif
from work.Work_Locomotif import Work_Locomotif
from data.Rundata_Locomotif import Rundata_Locomotif
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
        # Ui_Locomotif knows setupUi and retranslateUi methods
        self.ui.setupUi(self)

        # load tools
        self.tools = Tools_Locomotif()
        self.tools.setupTools(self)
        # rundata = Rundata_Locomotif()
        rundata.setupRundata(self)
        # load work
        self.work = Work_Locomotif()
        self.work.setupWork(self,self.ui)
        
		# more initialisations
        self.ui.mainDataDisplay.setTabText(0,"Datensatz1")
        self.ui.mainDataDisplay.setTabText(1,"Datensatz2")

# These are custom slots used within Qt Designer

    def openDataFile(self, Locomotif):
		""" Load a Data File for Further Processing """
		dataFilename = self.tools.selectDataFile(self)
		if dataFilename == "":
			self.msgBox = QtGui.QMessageBox(None)
			self.msgBox.setText("NO FILE SELECTED")
			self.msgBox.exec_()
			return 0
		
		# store nme in global data	
		rundata.setDataFileName( self, dataFilename )
		self.ui.loadedDataFilename.setText(dataFilename);
		self.ui.t1LoadedDataFilename.setText(dataFilename);
		# create data frame
		df = loc.read_csv( str(dataFilename), mapsta_version=100)
		rundata.setDF(self, df )
		# and locomotif cluster object
		c = loc.Cluster(df)
		rundata.setCluster( self, c )
		self.ui.t1LoadedDatasets.setText(str(c.getDatasets()));
		# Daten fuer Polygone berechnen
		res11, ref = c.voronoi('biomass')
		rundata.setVoronoi1( self, res11, ref )
		res12, ref = c.voronoi('diversity')
		rundata.setVoronoi2( self, res12, ref )
		# initial values for maps
		mapWidth = 700
		rundata.setMapWidth( self, mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = 500
		rundata.setMapHeight( self, mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))
		map1Filename = "C:/user/thomas.sonstiges/GitHub/results/map1_v.png"
		map2Filename = "C:/user/thomas.sonstiges/GitHub/results/map2_v.png"
		rundata.setV1Mapname( self, map1Filename )
		rundata.setV2Mapname( self, map2Filename )
		# create new maps for current cluster
		loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=map1Filename )		
		loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12, out_path=map2Filename )	
		# Show Maps
		scene1 = QtGui.QGraphicsScene();
		scene1.addPixmap( QtGui.QPixmap(map1Filename) )
		self.ui.t14MapView.setScene(scene1);
		scene2 = QtGui.QGraphicsScene();
		scene2.addPixmap( QtGui.QPixmap(map2Filename) )
		self.ui.t15MapView.setScene(scene2);
		rundata.debugRundata()
		return 1

    def openGPSFile(self, Locomotif):
		""" Load a GPS File for Further Processing """
		gpsFileName = self.tools.selectGPSFile(self)

    def openProjectFile(self, Locomotif):
		""" Load a Project File for Further Processing """
		projectFileName = self.tools.selectProjectFile(self)

    def doReadCSV(self, Locomotif):
		"""
		Reload the CSV DataFrames with the given name
		"""
		self.work.workReadCSV( self, rundata )

    def doCreateCluster(self, Locomotif):
		"""
		Create Cluster for the loaded Dataframe
		"""
		self.work.workCreateCluster( self, rundata )

    def doCreatePolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreatePolygone(self, rundata )

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