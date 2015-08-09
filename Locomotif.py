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
        
        # create font for data display
        dataFont = QtGui.QFont()
        dataFont.setStyleHint(QtGui.QFont.Courier)
        rundata.setDataFont( self, dataFont )
		
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
		# load and display initial data
		self.work.readDataFileIntoTable( self, dataFilename )
		self.work.markDataOnGoogleMap( self, dataFilename )
		
		# initial names for maps
		mapv1Filename = "C:/user/thomas.sonstiges/GitHub/results/map1_v.png"
		mapv2Filename = "C:/user/thomas.sonstiges/GitHub/results/map2_v.png"
		rundata.setV1Mapname( self, mapv1Filename )
		rundata.setV2Mapname( self, mapv2Filename )
		mapd1Filename = "C:/user/thomas.sonstiges/GitHub/results/map1_d.png"
		mapd2Filename = "C:/user/thomas.sonstiges/GitHub/results/map2_d.png"
		rundata.setD1Mapname( self, mapd1Filename )
		rundata.setD2Mapname( self, mapd2Filename )
		# initial values for maps
		mapWidth = 700
		rundata.setMapWidth( self, mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = 500
		rundata.setMapHeight( self, mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))
		
		return 1
		
		# create data frame
		df = loc.read_csv( str(dataFilename), mapsta_version=100)
		rundata.setDF(self, df )
		self.ui.t1DataFrameView.setCurrentFont(rundata.getDataFont(self))
		self.ui.t1DataFrameView.setText( str(df) )
		# and locomotif cluster object
		c = loc.Cluster(df)
		rundata.setCluster( self, c )
		self.ui.t1LoadedDatasets.setText(str(c.getDatasets()))
		# Daten fuer Polygone berechnen
		res11, ref = c.voronoi('biomass')
		rundata.setVoronoi1( self, res11, ref )
		self.ui.t1Polygon1View.setText( str(res11) )
		res12, ref = c.voronoi('diversity')
		rundata.setVoronoi2( self, res12, ref )
		self.ui.t1Polygon2View.setText( str(res12) )
		# create new maps for current cluster
		loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=mapv1Filename )		
		loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12, out_path=mapv2Filename )	
		# Show Maps
		scene1 = QtGui.QGraphicsScene();
		scene1.addPixmap( QtGui.QPixmap(mapv1Filename) )
		self.ui.t1Map1View.setScene(scene1);
		scene2 = QtGui.QGraphicsScene();
		scene2.addPixmap( QtGui.QPixmap(mapv2Filename) )
		self.ui.t1Map2View.setScene(scene2);
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
		df = rundata.getDF( self )
		self.work.putCSVIntoTable( self, df )

    def doCreateCluster(self, Locomotif):
		"""
		Create Cluster for the loaded Dataframe
		"""
		self.work.workCreateCluster( self, rundata )
		c = rundata.getCluster( self )
		self.ui.t1LoadedDatasets.setText(str(c.getDatasets()))

    def doCreateVPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateVPolygone(self, rundata )
		res11 = rundata.getVoronoi1( self );
		res12 = rundata.getVoronoi2( self );
		self.ui.t1Polygon1View.setText( str(res11) )
		self.ui.t1Polygon2View.setText( str(res12) )

    def doCreateDPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateDPolygone(self, rundata )
		res11 = rundata.getDelaunay1( self );
		res12 = rundata.getDelaunay2( self );
		self.ui.t1Polygon1View.setText( str(res11) )
		self.ui.t1Polygon2View.setText( str(res12) )

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