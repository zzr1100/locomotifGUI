# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui;
import locomotif as loc

class Work_Locomotif(object):
    """
    Docstring
    """
    def setupWork(self, Locomotif, ui):
		self.initialized = 1
		self.ui = ui
    	
    def workReadCSV(self, Locomotif, rundata):
		"""
		Get the selected Data File Name and read as CSV
		"""
		dataFilename = self.ui.t1LoadedDataFilename.text();
		# create data frame
		df = loc.read_csv( str(dataFilename), mapsta_version=100)
		rundata.setDF(self, df )

    def workCreateCluster(self, Locomotif, rundata):
		"""
		Create Cluster for the loaded Dataframe
		"""
		df = rundata.getDF( self )
		# create locomotif cluster object
		c = loc.Cluster(df)
		rundata.setCluster( self, c )
		self.ui.t1LoadedDatasets.setText(str(c.getDatasets()))

    def workCreatePolygone(self, Locomotif, rundata):
		"""
		Create Polygone from given cluster
		"""
		c = rundata.getCluster( self )
		# Daten fuer Polygone berechnen
		res11, ref = c.voronoi('biomass')
		rundata.setVoronoi1( self, res11, ref )
		res12, ref = c.voronoi('diversity')
		rundata.setVoronoi2( self, res12, ref )

    def workCreateMaps(self, Locomotif, rundata):
		"""
		ReCreate the Maps for the loaded Datasets
		Us sizes from input fields
		"""
		# new size form input fields
		mapWidth, okw = self.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = self.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( self, mapWidth )
		rundata.setMapHeight( self, mapHeight )
		# stored filename
		map1Filename = rundata.getV1Mapname( self )
		map2Filename = rundata.getV2Mapname( self )
		# stored polygons
		res11 = rundata.getVoronoi1( self );
		res12 = rundata.getVoronoi1( self );
		rundata.debugRundata()
		# create new maps for current cluster
		loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=map1Filename )		
		loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=map2Filename )	
		# Show Maps
		scene1 = QtGui.QGraphicsScene();
		scene1.addPixmap( QtGui.QPixmap(map1Filename) )
		self.ui.t14MapView.setScene(scene1);
		scene2 = QtGui.QGraphicsScene();
		scene2.addPixmap( QtGui.QPixmap(map2Filename) )
		self.ui.t15MapView.setScene(scene2);
		rundata.debugRundata()
		