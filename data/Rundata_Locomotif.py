# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
#from PyQt4 import QtCore, QtGui;

class Rundata_Locomotif(object):
	"""
	Docstring
	"""
	def setupRundata(self):
		self.datafilename = ""
		self.gpsfilename = ""
		self.projectfilename = ""
		self.df = None
		self.cluster = None
		self.voronoi1values = None
		self.voronoi1ref = None
		self.voronoi2values = None
		self.voronoi2ref = None
		self.delaunay1values = None
		self.delaunay1ref = None
		self.delaunay2values = None
		self.delaunay2ref = None
		self.mapwidth = 0
		self.mapheight = 0
		self.mapv1filename = ""
		self.mapv2filename = ""
		self.mapd1filename = ""
		self.mapd2filename = ""
		self.googlemapwidth = 0
		self.googlemapheight = 0
		self.google1maptype = "hybrid"
		self.google2maptype = "hybrid"

	def debugRundata(self):
		print "DataFilename = " + self.datafilename
		print "GPSFilename = " + self.gpsfilename
		print "ProjectFilename = " + self.projectfilename
		print "Map Width = " + str(self.mapwidth)
		print "Map Height = " + str(self.mapheight)
		print "MapV1Filename = " + self.mapv1filename
		print "MapV2Filename = " + self.mapv2filename
		print "MapD1Filename = " + self.mapd1filename
		print "MapD2Filename = " + self.mapd2filename
		print "Google Map Width = " + str(self.googlemapwidth)
		print "Google Map Height = " + str(self.googlemapheight)
		print "Google1Maptype = " + self.google1maptype
		print "Google2Maptype = " + self.google2maptype
		print "DataFrame = "
		print self.df
		if self.cluster != None:
			print "Cluster Datasets = " + str(self.cluster.getDatasets())
		else:
			print "No Cluster data present"
		print "Voronoi1 REF = "
		print self.voronoi1ref
		print "Voronoi1 values = "
		print self.voronoi1values
		print "Voronoi2 REF = "
		print self.voronoi2ref
		print "Voronoi2 values = "
		print self.voronoi2values
		print "Delaunay1 REF = "
		print self.delaunay1ref
		print "Delaunay1 values = "
		print self.delaunay1values
		print "Delaunay2 REF = "
		print self.delaunay2ref
		print "Delaunay2 values = "
		print self.delaunay2values

	def cleanBuffer( self ):
		print "Clean RUndata"
		self.datafilename = ""
		self.gpsfilename = ""
		self.projectfilename = ""
		self.df = None
		self.cluster = None
		self.voronoi1values = None
		self.voronoi1ref = None
		self.voronoi2values = None
		self.voronoi2ref = None
		self.delaunay1values = None
		self.delaunay1ref = None
		self.delaunay2values = None
		self.delaunay2ref = None
		self.mapwidth = 0
		self.mapheight = 0
		self.mapv1filename = ""
		self.mapv2filename = ""
		self.mapd1filename = ""
		self.mapd2filename = ""
		# leave these current values
		# self.googlemapwidth = 0
		# self.googlemapheight = 0
		#self.google1Maptype = "hybrid"
		#self.google2Maptype = "hybrid"
	
	def setDataFont( self, font ):
		self.datafont = font

	def getDataFont( self ):
		return self.datafont

	def setDataFileName( self, fname ):
		self.datafilename = str(fname)

	def getDataFileName( self ):
		return self.datafilename
		
	def setGpsFileName( self, fname ):
		self.gpsfilename = str(fname)

	def setProjectFileName( self, fname ):
		self.projectfilename = str(fname)
		
	def setDF( self, df ):
		self.df = df		

	def getDF( self ):
		return self.df		

	def setCluster( self, cluster ):
		self.cluster = cluster	

	def getCluster( self ):
		return self.cluster

	def setVoronoi1( self, res, ref ):
		self.voronoi1values = res
		self.voronoi1ref = str(ref)

	def getVoronoi1( self ):
		return self.voronoi1values

	def setVoronoi2( self, res, ref ):
		self.voronoi2values = res	
		self.voronoi2ref = str(ref)

	def getVoronoi2( self ):
		return self.voronoi2values	

	def setDelaunay1( self, res, ref ):
		self.delaunay1values = res
		self.delaunay1ref = str(ref)

	def getDelaunay1( self ):
		return self.delaunay1values

	def setDelaunay2( self, res, ref ):
		self.delaunay2values = res	
		self.delaunay2ref = str(ref)

	def getDelaunay2( self ):
		return self.delaunay2values	

	def setMapWidth( self, w ):
		self.mapwidth = w

	def getMapWidth( self ):
		return self.mapwidth
		
	def setMapHeight( self, h ):
		self.mapheight = h

	def getMapHeight( self ):
		return self.mapheight
		
	def setV1Mapname( self, filename ):
		self.mapv1filename = filename

	def getV1Mapname( self ):
		return self.mapv1filename

	def setV2Mapname( self, filename ):
		self.mapv2filename = filename

	def getV2Mapname( self ):
		return self.mapv2filename

	def setD1Mapname( self, filename ):
		self.mapd1filename = filename

	def getD1Mapname( self ):
		return self.mapd1filename

	def setD2Mapname( self, filename ):
		self.mapd2filename = filename

	def getD2Mapname( self ):
		return self.mapd2filename

	def setGoogleMapWidth( self, w ):
		self.googlemapwidth = w

	def getGoogleMapWidth( self ):
		return self.googlemapwidth
		
	def setGoogleMapHeight( self, h ):
		self.googlemapheight = h

	def getGoogleMapHeight( self ):
		return self.googlemapheight

	def setGoogle1Maptype( self, maptype ):
		self.google1maptype = maptype

	def getGoogle1Maptype( self ):
		return self.google1maptype

	def setGoogle2Maptype( self, maptype ):
		self.google2maptype = maptype

	def getGoogle2Maptype( self ):
		return self.google2maptype

		
		