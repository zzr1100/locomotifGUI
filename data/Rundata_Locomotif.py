# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui;

class Rundata_Locomotif(object):
	"""
	Docstring
	"""
	def setupRundata(self, Locomotif):
		self.dataFilename = ""
		self.gpsFilename = ""
		self.projectFilename = ""

	def debugRundata(self):
		print "DataFilename = " + self.datafilename
		print "GPSFilename = " + self.gpsFilename
		print "ProjectFilename = " + self.projectFilename
		print "DataFrame = "
		print self.df
		print "Cluster Datasets = "
		print self.cluster.getDatasets()
		print "Voronoi1 REF = " + self.voronoi1ref
		print "Voronoi1 values = "
		print self.voronoi1values
		print "Voronoi2 REF = " + self.voronoi2ref
		print "Voronoi2 values = "
		print self.voronoi2values
		print "Map Width = " + str(self.mapwidth)
		print "Map Height = " + str(self.mapheight)
		print "Map1Filename = " + self.map1filename
		print "Map2Filename = " + self.map2filename

	def setDataFileName( self, loc, fname ):
		self.datafilename = str(fname)

	def setGpsFileName( self, loc, fname ):
		self.gpsFilename = str(fname)

	def setProjectFileName( self, loc, fname ):
		self.projectFilename = str(fname)
		
	def setDF( self, loc, df ):
		self.df = df		
		
	def setCluster( self, loc, cluster ):
		self.cluster = cluster	

	def setVoronoi1( self, loc, res, ref ):
		self.voronoi1values = res
		self.voronoi1ref = str(ref)

	def getVoronoi1( self, loc ):
		return self.voronoi1values

	def setVoronoi2( self, loc, res, ref ):
		self.voronoi2values = res	
		self.voronoi2ref = str(ref)

	def getVoronoi2( self, loc ):
		return self.voronoi2values	

	def setMapWidth( self, loc, w ):
		self.mapwidth = w
		
	def setMapHeight( self, loc, h ):
		self.mapheight = h
		
	def setV1Mapname( self, loc, filename ):
		self.map1filename = filename

	def getV1Mapname( self, loc ):
		return self.map1filename

	def setV2Mapname( self, loc, filename ):
		self.map2filename = filename

	def getV2Mapname( self, loc ):
		return self.map2filename


		
		