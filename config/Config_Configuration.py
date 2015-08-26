# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
import os
from PyQt4 import QtCore, QtGui;

class Config_Configuration(object):
	"""
	Docstring
	"""
	def setupConfig(self):
		self.dataPath = ""
		self.mapPath = ""
		self.mapWidth = 700
		self.mapHeight = 550
		self.googleMapWidth = 700
		self.googleMapHeight = 550
		self.google1Maptype = "hybrid"
		self.google2Maptype = "hybrid"
		self.dataFont = None

	def debugConfig(self):
		print "-------------------------------------"
		print "Global Configuration Data"
		print "-------------------------------------"
		print "DataPath = " + self.dataPath
		print "MapPath = " + self.mapPath
		print "MapWidth = " + str(self.mapWidth)
		print "MapHeight = " + str(self.mapHeight)
		print "GoogleMapWidth = " + str(self.googleMapWidth)
		print "GoogleMapHeight = " + str(self.googleMapHeight)
		print "Google 1 Maptype = " + self.google1Maptype
		print "Google 2 Maptype = " + self.google2Maptype

	def initConfig(self, homePath):
		# read configuration file
		cfgPath = homePath + "\\etc"
		cfgFile = cfgPath + "\\lcGui.resources"
		# TODO READ
		parentDir = os.path.dirname( homePath )
		self.dataPath = parentDir + "\\sample_data"
		self.mapPath = parentDir + "\\results"
		self.mapWidth = 700
		self.mapHeight = 550
		self.googleMapWidth = 700
		self.googleMapHeight = 550
		self.google1Maptype = "hybrid"
		self.google2Maptype = "hybrid"
		self.dataFont = QtGui.QFont()
		self.dataFont.setStyleHint(QtGui.QFont.Courier)

	def getDataFont( self ):
		return self.dataFont
		
	def setDataPath( self, path ):
		self.dataPath = path

	def getDataPath( self ):
		return self.dataPath

	def setMapPath( self, path ):
		self.mapPath = path

	def getMapPath( self ):
		return self.mapPath

	def setMapWidth( self, width ):
		self.mapWidth = width

	def getMapWidth( self ):
		return self.mapWidth

	def setMapHeight( self, height ):
		self.mapHeight = height

	def getMapHeight( self ):
		return self.mapHeight

	def setGoogleMapWidth( self, width ):
		self.googleMapWidth = width

	def getGoogleMapWidth( self ):
		return self.googleMapWidth

	def setGoogleMapHeight( self, height ):
		self.googleMapHeight = height

	def getGoogleMapHeight( self ):
		return self.googleMapHeight

	def setGoogle1Maptype( self, maptype ):
		self.google1Maptype = maptype

	def getGoogle1Maptype( self ):
		return self.google1Maptype

	def setGoogle2Maptype( self, maptype ):
		self.google2Maptype = maptype

	def getGoogle2Maptype( self ):
		return self.google2Maptype

		
# Global Config Data to be used throughout the application
		
configData = Config_Configuration()

		