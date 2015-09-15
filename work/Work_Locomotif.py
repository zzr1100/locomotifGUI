# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui, QtWebKit
import locomotif as loc
from tools.Tools_Locomotif import Tools_Locomotif

class Work_Locomotif(object):
    """
    Docstring
    """
    def setupWork(self):
		self.initialized = 1
		self.tools = Tools_Locomotif()
		self.tools.setupTools()

    def workCleanTabs(self, widgets, rundata):
		""" 
		Depending on the working state clean the tabs that do
		not yet contain current data
		"""
		cleanLevel = rundata.getWorkingState()
		#print "Clean Tabs level " + str(cleanLevel)
		if cleanLevel<1:
			rundata.cleanBuffer()
			#print "Clean Tabs data"
			widgets.t1FileDataView.clear()
			widgets.t1GoogleMapsView.load( QtCore.QUrl("about:blank"))
			widgets.t1Data.setTabEnabled(0,False)
			widgets.t1Data.setTabEnabled(1,False)
		if cleanLevel<4:
			#print "Clean Tabs csv"
			widgets.t1DataFrameView.clear()
			widgets.t1Data.setTabEnabled(2,False)
		if cleanLevel<7:
			#print "Clean Tabs poly"
			widgets.t1Polygon1View.clear()
			widgets.t1Polygon2View.clear()
			widgets.t1GoogleMaps2View.load( QtCore.QUrl("about:blank"))
			widgets.t1Data.setTabEnabled(3,False)
			widgets.t1Data.setTabEnabled(4,False)
			widgets.t1Data.setTabEnabled(5,False)
			rundata.setPolygonType(0)
		if cleanLevel<9:
			#print "Clean Tabs map"
			scene = QtGui.QGraphicsScene();
			widgets.t1Map1View.setScene(scene);
			widgets.t1Map2View.setScene(scene);
			widgets.t1Data.setTabEnabled(6,False)
			widgets.t1Data.setTabEnabled(7,False)
		
    def readDataFileIntoTable(self, widgets, rundata, filePathAndName ):
		""" 
		Function to display textfile in table 
		"""
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		# clear table 
		widgets.t1FileDataView.clear()
		initRowCount = widgets.t1FileDataView.rowCount()
		# read headert line with table names
		line = istream.readLine()
		fields = line.split(';')
		numofcols = fields.count()
		widgets.t1FileDataView.setHorizontalHeaderLabels( fields )
		widgets.t1FileDataView.setColumnWidth(0,140)
		widgets.t1FileDataView.setColumnWidth(1,140)
		# read data lines
		rowIndex = 0
		while (not istream.atEnd()):
			line = istream.readLine()
			values = line.split(';')
			numofcols = values.count()
			if rowIndex>=initRowCount:
				widgets.t1FileDataView.insertRow(rowIndex)
			widgets.t1FileDataView.setRowHeight(rowIndex,22)
			colIndex = 0
			for value in values:
				item = QtGui.QTableWidgetItem()
				item.setText( str(value) )
				widgets.t1FileDataView.setItem( rowIndex, colIndex, item )
				# print "Zelle " + str(colIndex) + " / "+ str(rowIndex)+" = " + value
				colIndex = colIndex+1
			rowIndex = rowIndex+ 1
		fhdl.close()
		widgets.t1Data.setTabEnabled(0,True)
		rundata.setWorkingState(2)

    def markDataOnGoogleMap(self, widgets, rundata):
		""" display google map with data points marked """
		# new size form input fields
		mapWidth, okw = widgets.t1GMMapWidth.text().toInt(10)
		mapHeight, okh = widgets.t1GMMapHeight.text().toInt(10)
		rundata.setGoogleMapWidth( mapWidth )
		rundata.setGoogleMapHeight( mapHeight )
		# prepare GOOGLE MAPS url
		maphint = widgets.t1GoogleMapsHint
		map = widgets.t1GoogleMapsView
		url = "http://maps.google.com/maps/api/staticmap?sensor=false&language=de"
		url = url + "&size="+str(mapWidth)+"x"+str(mapHeight)
		url = url + "&maptype=" + rundata.getGoogle1Maptype()
		# read file and append markers
		fhdl = QtCore.QFile(rundata.getDataFileName())
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		# skip header line
		line = istream.readLine()
		numl = 0
		nump = 0
		while (not istream.atEnd()):
			line = istream.readLine()
			numl = numl + 1
			values = line.split(';')
			#print "marker-lat = " + values[0]
			#print "marker-lon = " + values[1]
			urlpart = "&markers="+str(values[0])+","+str(values[1])
			if (len(url)+len(urlpart)) < 1850:
				url = url + "&" + urlpart
				nump = nump + 1	
			
		# display
		print url
		map.load( QtCore.QUrl(url))
		# display a hint if not all lines are displayed in the map
		if nump < numl:
			maphint.setText("ATTENTION: Big data, not all points may be displayed at the same time")
		if rundata.getWorkingState()<3:
			rundata.setWorkingState(3)
		widgets.t1Data.setTabEnabled(1,True)

    def workReadCSV(self, widgets, rundata):
		"""
		Get the selected Data File Name and read as CSV
		"""
		if rundata.getWorkingState()<2:
			self.tools.showInfo( "Error", "SELECT AND LOAD INPUT FILE FIRST" )
			return
		dataFilename = widgets.t1LoadedDataFilename.text();
		if dataFilename == "":
			self.tools.showInfo( "Info", "SELECT INPUT FILE FIRST" )
			return
			
		# create data frame
		try:
			df = loc.read_csv( str(dataFilename), mapsta_version=100)
		except Exception, e:
			self.tools.showInfo("Exception from locomotif packet", str(e) )
			return
		rundata.setDF(df)
		rundata.setWorkingState(4)

    def putCSVIntoTable(self, widgets, rundata, df ):
		""" Function display CSV in table """
		# clear table 
		widgets.t1DataFrameView.clear()
		initRowCount = widgets.t1DataFrameView.rowCount()
		# set table header
		colIndex = 0
		for col in df.columns:
			item = QtGui.QTableWidgetItem()
			item.setText( str(col) )
			widgets.t1DataFrameView.setHorizontalHeaderItem( colIndex, item )
			colIndex = colIndex+1
		widgets.t1DataFrameView.setColumnWidth(2,260)
		# display data lines
		rowIndex = 0
		for value in df.values:
			if rowIndex>=initRowCount:
				widgets.t1DataFrameView.insertRow(rowIndex)
			widgets.t1DataFrameView.setRowHeight(rowIndex,22)
			colIndex = 0
			# df object has always 3 columns
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[0]) )
			widgets.t1DataFrameView.setItem( rowIndex, colIndex, item )
			colIndex = colIndex+1
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[1]) )
			widgets.t1DataFrameView.setItem( rowIndex, colIndex, item )
			colIndex = colIndex+1
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[2]) )
			widgets.t1DataFrameView.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1
		rundata.setWorkingState(5)
		widgets.t1Data.setTabEnabled(2,True)
		widgets.t1Data.setCurrentIndex(2)

    def workCreateCluster(self, widgets, rundata):
		"""
		Create Cluster for the loaded Dataframe
		"""
		df = rundata.getDF()
		
		# create locomotif cluster object
		c = loc.Cluster(df)
		rundata.setCluster( c )
		widgets.t1LoadedDatasets.setText(str(c.getDatasets()))
		rundata.setWorkingState(6)
		widgets.t1Data.setCurrentIndex(2)
		# clean existing polygones and maps
		self.workCleanTabs( widgets, rundata )

    def workCreateVPolygone(self, widgets, rundata):
		"""
		Create Polygone from given cluster
		"""
		if rundata.getWorkingState()<2:
			self.tools.showInfo( "Error", "SELECT AND LOAD INPUT FILE FIRST" )
			return
		if rundata.getWorkingState()<6:
			self.tools.showInfo( "Error", "FIRST YOU HAVE TO READ CSV AND CREATE DATASETS" )
			return

		c = rundata.getCluster()

		# calculate polynoms
		try:
			res11, ref = c.voronoi('biomass')
		except Exception, e:
			self.tools.showInfo("Exception from locomotif packet", str(e) )
			return
		rundata.setVoronoi1( res11, ref )
		try:
			res12, ref = c.voronoi('diversity')
		except Exception, e:
			self.tools.showInfo("Exception from locomotif packet", str(e) )
			return
		rundata.setVoronoi2( res12, ref )
		# display
		self.putPolygonIntoTable( res11, widgets.t1Polygon1View, rundata.getDataFont() )
		self.putPolygonIntoTable( res12, widgets.t1Polygon2View, rundata.getDataFont() )
		rundata.setPolygonType(1)
		rundata.setWorkingState(7)
		widgets.t1Data.setTabEnabled(3,True)
		widgets.t1Data.setTabEnabled(4,True)
		widgets.t1Data.setCurrentIndex(3)
		# clean existing maps
		self.workCleanTabs( widgets, rundata )

    def workCreateDPolygone(self, widgets, rundata):
		"""
		Create Polygone from given cluster
		"""
		if rundata.getWorkingState()<2:
			self.tools.showInfo( "Error", "SELECT AND LOAD INPUT FILE FIRST" )
			return
		if rundata.getWorkingState()<6:
			self.tools.showInfo( "Error", "FIRST YOU HAVE TO READ CSV AND CREATE DATASETS" )
			return
		
		c = rundata.getCluster()
		
		# Daten fuer Polygone berechnen
		try:
			res11, ref = c.delaunay('biomass')
		except Exception, e:
			self.tools.showInfo("Exception from locomotif packet", str(e) )
			return
		rundata.setDelaunay1( res11, ref )
		try:
			res12, ref = c.delaunay('diversity')
		except Exception, e:
			self.tools.showInfo("Exception from locomotif packet", str(e) )
			return
		rundata.setDelaunay2( res12, ref )
		# display
		self.putPolygonIntoTable( res11, widgets.t1Polygon1View, rundata.getDataFont() )
		self.putPolygonIntoTable( res12, widgets.t1Polygon2View, rundata.getDataFont() )
		rundata.setPolygonType(2)
		rundata.setWorkingState(7)
		widgets.t1Data.setTabEnabled(3,True)
		widgets.t1Data.setTabEnabled(4,True)
		widgets.t1Data.setCurrentIndex(3)
		# clean existing maps
		self.workCleanTabs( widgets, rundata )

    def putPolygonIntoTable(self, pres, uiTable, font ):
		""" Function display Polygone in table """
		# clear table 
		uiTable.clear()
		# set table header
		item = QtGui.QTableWidgetItem()
		item.setText( "Geometry" )
		uiTable.setHorizontalHeaderItem( 0, item )
		item = QtGui.QTableWidgetItem()
		item.setText( "Value" )
		uiTable.setHorizontalHeaderItem( 1, item )
		uiTable.setColumnWidth(0,500)

		rowIndex = 0
		initRowCount = uiTable.rowCount()
		for geomvalue in pres.geometry:
			if rowIndex>=initRowCount:
				uiTable.insertRow(rowIndex)
			uiTable.setRowHeight(rowIndex,22)
			colIndex = 0
			# table has 2 columns
			item = QtGui.QTableWidgetItem()
			item.setText( str(geomvalue) )
			uiTable.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1
		
		rowIndex = 0
		initRowCount = uiTable.rowCount()
		for value in pres.value:
			if rowIndex>=initRowCount:
				uiTable.insertRow(rowIndex)
			uiTable.setRowHeight(rowIndex,22)
			colIndex = 1
			# table has 2 columns
			item = QtGui.QTableWidgetItem()
			item.setFont(font)
			item.setText( str(value) )
			uiTable.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1

    def markPolygonOnGoogleMap(self, widgets, rundata, pres):
		""" display google map with data points marked """
		# new size form input fields
		mapWidth, okw = widgets.t1GM2MapWidth.text().toInt(10)
		mapHeight, okh = widgets.t1GM2MapHeight.text().toInt(10)
		rundata.setGoogleMapWidth( mapWidth )
		rundata.setGoogleMapHeight( mapHeight )
		# prepare GOOGLE MAPS url
		maphint = widgets.t1GoogleMaps2Hint
		map = widgets.t1GoogleMaps2View
		url = "http://maps.google.com/maps/api/staticmap?sensor=false&language=de"
		url = url + "&size="+str(mapWidth)+"x"+str(mapHeight)
		url = url + "&maptype=" + rundata.getGoogle2Maptype()
		# scan polygone and append markers
		num = 0
		for geomvalue in pres.geometry:
			# transform polygon (geomvalue) into googlemaps path
			# sample
			# POLYGON ((LON           LAT,
			#           7.88942045146 47.990827281500003,
			#           7.86850930989 48.003640800699998,
			#           7.86510335449 48.001608965734277,
			#           7.86510335449 47.988457948584305,
			#           7.89045027516 47.982788794699999,
			#           7.88942045146 47.990827281500003
			#         ))
			line = str(geomvalue)
			line = line.replace( "POLYGON ((", "")
			line = line.replace( "))", "")
			# into googlepath
			# path=color:0x0000ff|weight:5|
			#   LAT      ,LON
			#   40.737102,-73.990318|
			#   40.749825,-73.987963|
			#   40.752946,-73.987384|
			#   40.755823,-73.986397

			# das waere die schnelle variante
			# die funktioniert jetzt aber nicht mehr weil die
			# koordinaten der Punkte vertausch werden muessen
			#line = line.replace( ",", "|")
			#line = line.replace( " ", ",")
			#urlpart = "path=color:0x0000ff|"+line
			
			# 2 variante mit weniger kommastellen der punkte
			#urlpart = "path=color:0x0000ff"
			#points = line.split(",")
			#for point in points:
			#	# point2 = point.replace(" ", ",")
			#	pvalues = point.split(" ")
			#	lonval = float( str('{:10.4f}'.format(float(pvalues[0]))) )
			#	latval = float( str('{:10.4f}'.format(float(pvalues[1]))) )
			#	urlpart = urlpart + '|' + str(latval) + "," + str(lonval)
			
			# 3 variante mit codierten paths
			encodedPath = self.tools.encodeGoogleMapsPath(line)
			urlpart = "path=enc:" + encodedPath
			
			# total path length must be < 2048
			# internal conversion to cgi causes special chars to be length 3
			# so we calculate with a len < 1850
			# if num < 29:
			if (len(url)+len(urlpart)) < 1850:
				url = url + "&" + urlpart
				num = num + 1	

		# display
		map.load( QtCore.QUrl(url))
		# display a hint if not all lines are displayed in the map
		if num < len(pres.geometry):
			print "#num polygones = " + str(len(pres.geometry))
			print "#num in display = " + str(num)
			hint = "ATTENTION: Big data, url too long, only "+str(num)+" of "+str(len(pres.geometry))+" polygones displayed"
			maphint.setText( hint )
		else:
			maphint.setText("")
		rundata.setWorkingState(8)
		widgets.t1Data.setTabEnabled(5,True)

    def refreshPolygonOnGoogleMap(self, widgets, rundata ):
		print "refresh polygon"
		if rundata.getPolygonType()==1:
			print "mark polygon 1 " + str(rundata.getVoronoi1())
			self.markPolygonOnGoogleMap( widgets, rundata, rundata.getVoronoi1() )
			return
		if rundata.getPolygonType()==2:
			print "mark polygon 2 " + str(rundata.getDelaunay1())
			self.markPolygonOnGoogleMap( widgets, rundata, rundata.getDelaunay1() )
			return
	
    def workCreateMaps(self, locapp, widgets, rundata):
		"""
		ReCreate the Maps for the loaded Datasets
		Use sizes from input fields
		"""
		if rundata.getWorkingState()<2:
			self.tools.showInfo( "Error", "SELECT AND LOAD INPUT FILE FIRST" )
			return
		if rundata.getWorkingState()<6:
			self.tools.showInfo( "Error", "FIRST YOU HAVE TO READ CSV AND CREATE DATASETS" )
			return
		if rundata.getWorkingState()<8:
			self.tools.showInfo( "Error", "FIRST YOU HAVE TO CREATE POLYGONES" )
			return
		
		# new size form input fields
		mapWidth, okw = locapp.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = locapp.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( mapWidth )
		rundata.setMapHeight( mapHeight )
		# which polygons have been created
		if rundata.getPolygonType() == 0: 
				self.tools.showInfo( "Error", "FIRST YOU HAVE TO CALCULATE POLYNOMS" )
				return
		if rundata.getPolygonType() == 1: 
			# stored filenames
			map1Filename = rundata.getV1Mapname()
			map2Filename = rundata.getV2Mapname()
			# stored polygons
			res11org = rundata.getVoronoi1();
			res12org = rundata.getVoronoi2();
			# switch the point values, seems that the mapper
			# request points as (lon,lat) and not (lat,lon)
			# res11 = self.tools.modifyPolygonValues(res11org)
			# res12 = self.tools.modifyPolygonValues(res12org)
			res11 = res11org
			res12 = res12org
			# create new maps for current cluster
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=str(map1Filename) )
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=str(map2Filename) )

		if rundata.getPolygonType() == 2: 
			# stored filenames
			map1Filename = rundata.getD1Mapname()
			map2Filename = rundata.getD2Mapname()
			# stored polygons
			res11 = rundata.getDelaunay1();
			res12 = rundata.getDelaunay2();
			# create new maps for current cluster
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=str(map1Filename) )
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=str(map2Filename) )
			
		# Show Maps
		scene1 = QtGui.QGraphicsScene();
		scene1.addPixmap( QtGui.QPixmap(map1Filename) )
		widgets.t1Map1View.setScene(scene1);
		scene2 = QtGui.QGraphicsScene();
		scene2.addPixmap( QtGui.QPixmap(map2Filename) )
		widgets.t1Map2View.setScene(scene2);
		rundata.setWorkingState(9)
		widgets.t1Data.setTabEnabled(6,True)
		widgets.t1Data.setTabEnabled(7,True)
		widgets.t1Data.setCurrentIndex(6)
		
