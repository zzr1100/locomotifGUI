# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui;

DefaultFilter = "GPS Files (*.gps *.kml *.xml);;DataFiles (*.txt *.csv);;Project Files (*.prj *.py);;Images (*.png *.xpm *.jpg);;All Files (*.*)"
GPSFilter = "GPS Files (*.gps *.kml *.xml)"
DataFilter = "DataFiles (*.txt *.csv)"
ProjectFilter = "Project Files (*.prj *.py)"

class Tools_Locomotif(object):
    """
    Docstring
    """
    def setupTools(self, Locomotif):
    	self.currentFilename = "tbd"
    	
    def selectDataFile(self, Locomotif):
        return self.selectUserFile(self,"Data",DataFilter)

    def selectGPSFile(self, Locomotif):
        return self.selectUserFile(self,"GPS",GPSFilter)

    def selectProjectFile(self, Locomotif):
        return self.selectUserFile(self,"Project",ProjectFilter)

    def selectAnyFile(self, Locomotif):
        return self.selectUserFile(self,"Datei")
		
    def selectUserFile(self, Locomotif, fcaption, selectedFilter="*.*"):
		""" Function to select a filename from disk """
		self.ofDialog = QtGui.QFileDialog(None)
		self.selectedFileName = self.ofDialog.getOpenFileName(None, "Open "+fcaption+" File", ".", DefaultFilter, selectedFilter )
		'''
		self.msgBox = QtGui.QMessageBox(None)
		self.msgBox.setText("Selected Data-File was \"" + self.selectedFileName + "\"")
		self.msgBox.exec_()
		print "----Testausgabe Start"
		print self
		print self.ofDialog
		print self.msgBox
		print self.selectedFileName
		print "Testausgabe Ende-----"
		'''
		return self.selectedFileName

    def readDataFile(self, Locomotif, filePathAndName ):
		""" Function to read textfile from disk """
		result = QtCore.QString()
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		while (not istream.atEnd()):
			line = istream.readLine()
			result.append( line )
			result.append( "\n" )
		fhdl.close()
		return result


