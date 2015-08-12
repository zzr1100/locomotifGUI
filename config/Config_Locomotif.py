# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
import os
from PyQt4 import QtCore, QtGui;

class Config_Locomotif(object):
	"""
	Docstring
	"""
	def setupConfig(self, loc):
		self.dataPath = ""
		self.mapPath = ""
		self.mapWidth = 700
		self.mapHeight = 500

	def debugConfig(self):
		print "DataPath = " + self.dataPath
		print "MapPath = " + self.mapPath
		print "MapWidth = " + str(self.mapWidth)
		print "MapHeight = " + str(self.mapHeight)

	def initConfig(self, loc, homePath):
		# read configuration file
		cfgPath = homePath + "\\etc"
		cfgFile = cfgPath + "\\lcGui.resources"
		# TODO READ
		parentDir = os.path.dirname( homePath )
		self.dataPath = parentDir + "\\sample_data"
		self.mapPath = parentDir + "\\results"
		self.mapWidth = 700
		self.mapHeight = 500
		# display
		loc.ui.editCfgDataPath.setText(self.dataPath)
		loc.ui.editCfgMapPath.setText(self.mapPath)
		loc.ui.editCfgMapWidth.setText(str(self.mapWidth))
		loc.ui.editCfgMapHeight.setText(str(self.mapHeight))

	def readConfig(self, loc):
		# get values from input fields
		self.dataPath = loc.ui.editCfgDataPath.text()
		self.mapPath = loc.ui.editCfgMapPath.text()
		self.mapWidth = loc.ui.editCfgMapWidth.text().toInt(10)
		self.mapHeight = loc.ui.editCfgMapHeight.text().toInt(10)

	def storeConfig(self, loc):
		# get values from input fields
		self.dataPath = loc.ui.editCfgDataPath.text()
		self.mapPath = loc.ui.editCfgMapPath.text()
		self.mapWidth = loc.ui.editCfgMapWidth.text().toInt(10)
		self.mapHeight = loc.ui.editCfgMapHeight.text().toInt(10)
		# and store in file

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

	def selectDataPath( self, loc ):
		"""
		Function to select a directory on disk 
		"""
		os.chdir( str(self.dataPath) )
		ofDialog = QtGui.QFileDialog(None)
		selectedDirectory = ofDialog.getExistingDirectory(None, "Select Path for Data Files", "."  )
		if selectedDirectory== "":
			return
		self.dataPath = selectedDirectory
		loc.ui.editCfgDataPath.setText(self.dataPath)
		
	def selectMapPath( self, loc ):
		"""
		Function to select a directory on disk 
		"""
		os.chdir( str(self.mapPath) )
		ofDialog = QtGui.QFileDialog(None)
		selectedDirectory = ofDialog.getExistingDirectory(None, "Select Path for Maps", "."  )
		if selectedDirectory== "":
			return
		self.mapPath = selectedDirectory
		loc.ui.editCfgMapPath.setText(self.mapPath)
