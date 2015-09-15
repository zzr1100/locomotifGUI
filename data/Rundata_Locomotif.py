# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
#from PyQt4 import QtCore, QtGui;

# Values for Workingstate
# 0 = no data present
# 1 = datafile selected
# 2 = read into memory
# 3 = google map1 with data points created
# 4 = locomotif csv read executed and dataframe created
# 5 = dataframe loaded into display table
# 6 = locomotif cluster created
# 7 = locomotif polygones created ( V or D )
# 8 = google map2 with polygones created
# 9 = locomotif data maps created

class Rundata_Locomotif(object):
	"""
	Docstring
	"""
	def setupRundata(self):
		self.workingstate = 0
		self.datafilename = ""
		self.gpsfilename = ""
		self.projectfilename = ""
		self.df = None
		self.cluster = None
		self.polygontype = 0
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

	def debugRundata(self, title):
		print "-----------------------------------"
		print title + " = " + str(self)
		print "-----------------------------------"
		print "workingstate = " + str(self.workingstate)
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
		print "Polygontype = " + str(self.polygontype)
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
		self.workingstate = 0
		self.datafilename = ""
		self.gpsfilename = ""
		self.projectfilename = ""
		self.df = None
		self.cluster = None
		self.polygontype = 0
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
	
	def setWorkingState( self, workingstate ):
		self.workingstate = workingstate

	def getWorkingState( self ):
		return self.workingstate

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

	def setPolygonType( self, polygontype ):
		self.polygontype = polygontype

	def getPolygonType( self ):
		return self.polygontype
		
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

	def set_g_rundata( self ):
		"""
		Copy content from given rundata into g_rundata
		"""
		g_rundata.workingstate  = self.workingstate
		g_rundata.datafilename  = self.datafilename
		g_rundata.gpsfilename = self.gpsfilename
		g_rundata.projectfilename = self.projectfilename
		g_rundata.df = self.df
		g_rundata.cluster = self.cluster
		g_rundata.polygontype = self.polygontype
		g_rundata.voronoi1values = self.voronoi1values
		g_rundata.voronoi1ref = self.voronoi1ref
		g_rundata.voronoi2values = self.voronoi2values
		g_rundata.voronoi2ref = self.voronoi2ref
		g_rundata.delaunay1values = self.delaunay1values
		g_rundata.delaunay1ref = self.delaunay1ref
		g_rundata.delaunay2values = self.delaunay2values
		g_rundata.delaunay2ref = self.delaunay2ref
		g_rundata.mapwidth = self.mapwidth
		g_rundata.mapheight = self.mapheight
		g_rundata.mapv1filename = self.mapv1filename
		g_rundata.mapv2filename = self.mapv2filename
		g_rundata.mapd1filename = self.mapd1filename
		g_rundata.mapd2filename = self.mapd2filename
		g_rundata.googlemapwidth = self.googlemapwidth
		g_rundata.googlemapheight = self.googlemapheight
		g_rundata.google1maptype = self.google1maptype
		g_rundata.google2maptype = self.google2maptype

	def get_g_rundata( self ):
		"""
		Copy content from g_rundata into rundata instance
		"""
		self.workingstate = g_rundata.workingstate
		self.datafilename = g_rundata.datafilename
		self.gpsfilename = g_rundata.gpsfilename
		self.projectfilename = g_rundata.projectfilename
		self.df = g_rundata.df
		self.cluster = g_rundata.cluster
		self.polygontype = g_rundata.polygontype
		self.voronoi1values = g_rundata.voronoi1values
		self.voronoi1ref = g_rundata.voronoi1ref
		self.voronoi2values = g_rundata.voronoi2values
		self.voronoi2ref = g_rundata.voronoi2ref
		self.delaunay1values = g_rundata.delaunay1values
		self.delaunay1ref = g_rundata.delaunay1ref
		self.delaunay2values = g_rundata.delaunay2values
		self.delaunay2ref = g_rundata.delaunay2ref
		self.mapwidth = g_rundata.mapwidth
		self.mapheight = g_rundata.mapheight
		self.mapv1filename = g_rundata.mapv1filename
		self.mapv2filename = g_rundata.mapv2filename
		self.mapd1filename = g_rundata.mapd1filename
		self.mapd2filename = g_rundata.mapd2filename
		self.googlemapwidth = g_rundata.googlemapwidth
		self.googlemapheight = g_rundata.googlemapheight
		self.google1maptype = g_rundata.google1maptype
		self.google2maptype = g_rundata.google2maptype
		
# Global Rundata buffer to be used throughout the application
# The data from the selected tab is moved to this buffer
# "This buffer points to the selected data"
		
g_rundata = Rundata_Locomotif()

