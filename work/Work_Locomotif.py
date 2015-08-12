# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui, QtWebKit;
import locomotif as loc

class Work_Locomotif(object):
    """
    Docstring
    """
    def setupWork(self, Locomotif, ui):
		self.initialized = 1
		self.ui = ui
		self.lastcreated = 0

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

    def workCreateVPolygone(self, Locomotif, rundata):
		"""
		Create Polygone from given cluster
		"""
		c = rundata.getCluster( self )
		# Daten fuer Polygone berechnen
		res11, ref = c.voronoi('biomass')
		rundata.setVoronoi1( self, res11, ref )
		res12, ref = c.voronoi('diversity')
		rundata.setVoronoi2( self, res12, ref )
		self.lastcreated = 1

    def workCreateDPolygone(self, Locomotif, rundata):
		"""
		Create Polygone from given cluster
		"""
		c = rundata.getCluster( self )
		# Daten fuer Polygone berechnen
		res11, ref = c.delaunay('biomass')
		rundata.setDelaunay1( self, res11, ref )
		res12, ref = c.delaunay('diversity')
		rundata.setDelaunay2( self, res12, ref )
		self.lastcreated = 2

    def workCreateVMaps(self, Locomotif, rundata):
		# new size form input fields
		mapWidth, okw = self.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = self.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( self, mapWidth )
		rundata.setMapHeight( self, mapHeight )
		# stored polygons
		res11 = rundata.getVoronoi1( self );
		res12 = rundata.getVoronoi2( self );
		rundata.debugRundata()

    def workCreateDMaps(self, Locomotif, rundata):
		# new size form input fields
		mapWidth, okw = self.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = self.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( self, mapWidth )
		rundata.setMapHeight( self, mapHeight )
		# stored polygons
		res11 = rundata.getDelaunay1( self );
		res12 = rundata.getDelaunay2( self );
		rundata.debugRundata()

    def workCreateMaps(self, Locomotif, rundata):
		"""
		ReCreate the Maps for the loaded Datasets
		Use sizes from input fields
		"""
		# new size form input fields
		mapWidth, okw = self.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = self.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( self, mapWidth )
		rundata.setMapHeight( self, mapHeight )
		# which polygons have been created
		if self.lastcreated == 1: 
			# stored filenames
			map1Filename = rundata.getV1Mapname( self )
			map2Filename = rundata.getV2Mapname( self )
			# stored polygons
			res11 = rundata.getVoronoi1( self );
			res12 = rundata.getVoronoi2( self );
			# create new maps for current cluster
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=map1Filename )
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=map2Filename )

		if self.lastcreated == 2: 
			# stored filenames
			map1Filename = rundata.getD1Mapname( self )
			map2Filename = rundata.getD2Mapname( self )
			# stored polygons
			res11 = rundata.getDelaunay1( self );
			res12 = rundata.getDelaunay2( self );
			# create new maps for current cluster
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=map1Filename )
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=map2Filename )
			
		# Show Maps
		scene1 = QtGui.QGraphicsScene();
		scene1.addPixmap( QtGui.QPixmap(map1Filename) )
		self.ui.t1Map1View.setScene(scene1);
		scene2 = QtGui.QGraphicsScene();
		scene2.addPixmap( QtGui.QPixmap(map2Filename) )
		self.ui.t1Map2View.setScene(scene2);
		rundata.debugRundata()
		
    def readDataFileIntoTable(self, Locomotif, filePathAndName ):
		""" 
		Function to display textfile in table 
		"""
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		# clear table 
		self.ui.t1FileDataView.clear()
		initRowCount = self.ui.t1FileDataView.rowCount()
		# read headert line with table names
		line = istream.readLine()
		fields = line.split(';')
		numofcols = fields.count()
		self.ui.t1FileDataView.setHorizontalHeaderLabels( fields )
		self.ui.t1FileDataView.setColumnWidth(0,140)
		self.ui.t1FileDataView.setColumnWidth(1,140)
		# read data lines
		rowIndex = 0
		while (not istream.atEnd()):
			line = istream.readLine()
			values = line.split(';')
			numofcols = values.count()
			if rowIndex>=initRowCount:
				self.ui.t1FileDataView.insertRow(rowIndex)
			self.ui.t1FileDataView.setRowHeight(rowIndex,22)
			colIndex = 0
			for value in values:
				item = QtGui.QTableWidgetItem()
				item.setText( str(value) )
				self.ui.t1FileDataView.setItem( rowIndex, colIndex, item )
				# print "Zelle " + str(colIndex) + " / "+ str(rowIndex)+" = " + value
				colIndex = colIndex+1
			rowIndex = rowIndex+ 1
		fhdl.close()

    def markDataOnGoogleMap(self, Locomotif, filePathAndName):
		""" display google map with data points marked """
		# prepare GOOGLE MAPS url
		map = self.ui.t1GoogleMapsView
		url = "http://maps.google.com/maps/api/staticmap?maptype=hybrid&sensor=false&language=de"
		url = url + "&size=750x550"
		# read file and append markers
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		# skip header line
		line = istream.readLine()
		# take value form first line as center
		minlat = float(90)
		maxlat = float(-90)
		minlon = float(360)
		maxlon = float(0)
		while (not istream.atEnd()):
			line = istream.readLine()
			values = line.split(';')
			url = url + "&markers="+str(values[0])+","+str(values[1])
			lat = float(values[0])
			lon = float(values[1])
			if lat<minlat:
				minlat = lat
			if lat>maxlat:
				maxlat = lat
			if lon<minlon:
				minlon = lon
			if lon>maxlon:
				maxlon = lon
		# select center and zoom
		difflat = maxlat-minlat
		difflon = maxlon-minlon
		midlat = maxlat - difflat/2
		midlon = maxlon - difflon/2
		url = url + "&center="+str(midlat)+","+str(midlon)
		# zoomfaktor berechnen
		diff = difflat
		if difflon>difflat:
			diff = difflon
		zoom = 10
		if diff<=0.001:
			zoom = 17
		if diff>0.001 and diff<=0.1:
			zoom = 16
		if diff>0.01 and diff<=0.025:
			zoom = 15
		if diff>0.025 and diff<=0.05:
			zoom = 14
		if diff>0.05 and diff<=0.1:
			zoom = 13
		if diff>0.1 and diff<=0.2:
			zoom = 12
		if diff>0.2 and diff<=1:
			zoom = 11
		if diff>1 and diff<=2:
			zoom = 10
		if diff>2 and diff<=4:
			zoom = 9
		if diff>4 and diff<=8:
			zoom = 8
		if diff>8 and diff<=16:
			zoom = 7
		if diff>16:
			zoom = 6
		print difflat
		print difflon
		print zoom
		url = url + "&zoom="+str(zoom)
		# display
		map.load( QtCore.QUrl(url))

    def putCSVIntoTable(self, Locomotif, df ):
		""" Function display CSV in table """
		# clear table 
		self.ui.t1DataFrameView.clear()
		initRowCount = self.ui.t1DataFrameView.rowCount()
		# set table header
		colIndex = 0
		for col in df.columns:
			item = QtGui.QTableWidgetItem()
			item.setText( str(col) )
			self.ui.t1DataFrameView.setHorizontalHeaderItem( colIndex, item )
			colIndex = colIndex+1
		self.ui.t1DataFrameView.setColumnWidth(2,260)
		# display data lines
		rowIndex = 0
		for value in df.values:
			if rowIndex>=initRowCount:
				self.ui.t1DataFrameView.insertRow(rowIndex)
			self.ui.t1DataFrameView.setRowHeight(rowIndex,22)
			colIndex = 0
			# df object has always 3 columns
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[0]) )
			self.ui.t1DataFrameView.setItem( rowIndex, colIndex, item )
			colIndex = colIndex+1
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[1]) )
			self.ui.t1DataFrameView.setItem( rowIndex, colIndex, item )
			colIndex = colIndex+1
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[2]) )
			self.ui.t1DataFrameView.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1
