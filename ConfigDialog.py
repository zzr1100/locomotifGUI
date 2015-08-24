# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Mirko
"""
import sys
import os
from PyQt4 import QtGui, QtCore
from ui.Ui_Configuration import Ui_Configuration
from config.Config_Configuration import *

class ConfigDialog(QtGui.QDialog):
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
		self.cfgUi = Ui_Configuration()
		self.cfgUi.setupUi(self)

		# display current values from global config data
		self.displayCurrentValues()
		
	def reject(self):
		print "reject"
		# simply close the dialog
		self.hide()

	def accept(self):
		print "accept"
		# get values from dialog and store in global data
		configData.setDataPath( self.cfgUi.editCfgDataPath.text() )
		configData.setMapPath( self.cfgUi.editCfgMapPath.text() )
		hlptxt = self.cfgUi.editCfgMapWidth.text()
		hlpint, ok = hlptxt.toInt(10)
		configData.setMapWidth( hlpint )
		hlptxt = self.cfgUi.editCfgMapHeight.text()
		hlpint, ok = hlptxt.toInt(10)
		configData.setMapHeight( hlpint )
		
		hlptxt = self.cfgUi.editCfgMap2Width.text()
		hlpint, ok = hlptxt.toInt(10)
		configData.setGoogleMapWidth( hlpint )
		hlptxt = self.cfgUi.editCfgMap2Height.text()
		hlpint, ok = hlptxt.toInt(10)
		configData.setGoogleMapHeight( hlpint )

		hlptxt = self.cfgUi.editGoogle1Maptype.currentText()
		configData.setGoogle1Maptype(hlptxt)
		hlptxt = self.cfgUi.editGoogle2Maptype.currentText()
		configData.setGoogle2Maptype(hlptxt)

		configData.debugConfig()
		self.hide()

	def on_acceptButton_clicked(self):
		print "reject clicked"
		self.close()
        
	def on_rejectButton_clicked(self):
		print "accept clicked"
		self.close()
		
# These are custom slots used within Qt Designer

	def doSelectDataPath(self, ConfigDialog):
		os.chdir( configData.getDataPath() )
		ofDialog = QtGui.QFileDialog(None)
		selectedDirectory = ofDialog.getExistingDirectory(None, "Select Path for Data Files", "."  )
		if selectedDirectory== "":
			return
		configData.setDataPath(selectedDirectory)
		self.cfgUi.editCfgDataPath.setText(selectedDirectory)

	def doSelectMapPath(self, ConfigDialog):
		os.chdir( str(configData.getMapPath()) )
		ofDialog = QtGui.QFileDialog(None)
		selectedDirectory = ofDialog.getExistingDirectory(None, "Select Path for Maps", "."  )
		if selectedDirectory== "":
			return
		configData.setMapPath(selectedDirectory)
		self.cfgUi.editCfgMapPath.setText(selectedDirectory)

	def displayCurrentValues( self ):
		# display
		self.cfgUi.editCfgDataPath.setText(configData.getDataPath())
		self.cfgUi.editCfgMapPath.setText(configData.getMapPath())
		self.cfgUi.editCfgMapWidth.setText(str(configData.getMapWidth()))
		self.cfgUi.editCfgMapHeight.setText(str(configData.getMapHeight()))
		self.cfgUi.editCfgMap2Width.setText(str(configData.getGoogleMapWidth()))
		self.cfgUi.editCfgMap2Height.setText(str(configData.getGoogleMapHeight()))
		index = self.cfgUi.editGoogle1Maptype.findText(configData.getGoogle1Maptype())
		self.cfgUi.editGoogle1Maptype.setCurrentIndex(index)
		index = self.cfgUi.editGoogle2Maptype.findText(configData.getGoogle2Maptype())
		self.cfgUi.editGoogle2Maptype.setCurrentIndex(index)
		
	