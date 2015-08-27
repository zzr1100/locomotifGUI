# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Configuration.ui'
#
# Created: Thu Aug 27 14:58:45 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName(_fromUtf8("Configuration"))
        Configuration.resize(651, 277)
        self.buttonBox = QtGui.QDialogButtonBox(Configuration)
        self.buttonBox.setGeometry(QtCore.QRect(280, 220, 341, 32))
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_6 = QtGui.QLabel(Configuration)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(Configuration)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.editCfgMapPath = QtGui.QLineEdit(Configuration)
        self.editCfgMapPath.setGeometry(QtCore.QRect(140, 50, 411, 20))
        self.editCfgMapPath.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMapPath.setObjectName(_fromUtf8("editCfgMapPath"))
        self.editCfgDataPath = QtGui.QLineEdit(Configuration)
        self.editCfgDataPath.setGeometry(QtCore.QRect(140, 20, 411, 20))
        self.editCfgDataPath.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgDataPath.setObjectName(_fromUtf8("editCfgDataPath"))
        self.cmdSelCfgDataPath = QtGui.QPushButton(Configuration)
        self.cmdSelCfgDataPath.setGeometry(QtCore.QRect(560, 20, 75, 23))
        self.cmdSelCfgDataPath.setObjectName(_fromUtf8("cmdSelCfgDataPath"))
        self.cmdSelCfgMapPath = QtGui.QPushButton(Configuration)
        self.cmdSelCfgMapPath.setGeometry(QtCore.QRect(560, 50, 75, 23))
        self.cmdSelCfgMapPath.setObjectName(_fromUtf8("cmdSelCfgMapPath"))
        self.groupBox = QtGui.QGroupBox(Configuration)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 151, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 41, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.editCfgMapWidth = QtGui.QLineEdit(self.groupBox)
        self.editCfgMapWidth.setGeometry(QtCore.QRect(70, 20, 51, 20))
        self.editCfgMapWidth.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMapWidth.setObjectName(_fromUtf8("editCfgMapWidth"))
        self.editCfgMapHeight = QtGui.QLineEdit(self.groupBox)
        self.editCfgMapHeight.setGeometry(QtCore.QRect(70, 50, 51, 20))
        self.editCfgMapHeight.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMapHeight.setObjectName(_fromUtf8("editCfgMapHeight"))
        self.groupBox_2 = QtGui.QGroupBox(Configuration)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 80, 381, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 50, 41, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.editCfgMap2Width = QtGui.QLineEdit(self.groupBox_2)
        self.editCfgMap2Width.setGeometry(QtCore.QRect(70, 20, 51, 20))
        self.editCfgMap2Width.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMap2Width.setObjectName(_fromUtf8("editCfgMap2Width"))
        self.editCfgMap2Height = QtGui.QLineEdit(self.groupBox_2)
        self.editCfgMap2Height.setGeometry(QtCore.QRect(70, 50, 51, 20))
        self.editCfgMap2Height.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMap2Height.setObjectName(_fromUtf8("editCfgMap2Height"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(140, 20, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.editGoogle1Maptype = QtGui.QComboBox(self.groupBox_2)
        self.editGoogle1Maptype.setGeometry(QtCore.QRect(278, 20, 91, 22))
        self.editGoogle1Maptype.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editGoogle1Maptype.setObjectName(_fromUtf8("editGoogle1Maptype"))
        self.editGoogle1Maptype.addItem(_fromUtf8(""))
        self.editGoogle1Maptype.addItem(_fromUtf8(""))
        self.editGoogle1Maptype.addItem(_fromUtf8(""))
        self.editGoogle1Maptype.addItem(_fromUtf8(""))
        self.editGoogle2Maptype = QtGui.QComboBox(self.groupBox_2)
        self.editGoogle2Maptype.setGeometry(QtCore.QRect(278, 50, 91, 22))
        self.editGoogle2Maptype.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editGoogle2Maptype.setObjectName(_fromUtf8("editGoogle2Maptype"))
        self.editGoogle2Maptype.addItem(_fromUtf8(""))
        self.editGoogle2Maptype.addItem(_fromUtf8(""))
        self.editGoogle2Maptype.addItem(_fromUtf8(""))
        self.editGoogle2Maptype.addItem(_fromUtf8(""))

        self.retranslateUi(Configuration)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Configuration.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Configuration.reject)
        QtCore.QObject.connect(self.cmdSelCfgDataPath, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Configuration.doSelectDataPath)
        QtCore.QObject.connect(self.cmdSelCfgMapPath, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Configuration.doSelectMapPath)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(_translate("Configuration", "Settings", None))
        self.label_6.setText(_translate("Configuration", "Path for Map Files", None))
        self.label_5.setText(_translate("Configuration", "Path for Data Files", None))
        self.cmdSelCfgDataPath.setText(_translate("Configuration", "Browse", None))
        self.cmdSelCfgMapPath.setText(_translate("Configuration", "Browse", None))
        self.groupBox.setTitle(_translate("Configuration", "Map Dimesions", None))
        self.label_7.setText(_translate("Configuration", "Width:", None))
        self.label_8.setText(_translate("Configuration", "Height", None))
        self.groupBox_2.setTitle(_translate("Configuration", "Google Map Dimesions", None))
        self.label_9.setText(_translate("Configuration", "Width:", None))
        self.label_10.setText(_translate("Configuration", "Height", None))
        self.label.setText(_translate("Configuration", "Default Data Map Type:", None))
        self.label_2.setText(_translate("Configuration", "Default Polygon Map Type:", None))
        self.editGoogle1Maptype.setItemText(0, _translate("Configuration", "hybrid", None))
        self.editGoogle1Maptype.setItemText(1, _translate("Configuration", "satellite", None))
        self.editGoogle1Maptype.setItemText(2, _translate("Configuration", "roadmap", None))
        self.editGoogle1Maptype.setItemText(3, _translate("Configuration", "terrain", None))
        self.editGoogle2Maptype.setItemText(0, _translate("Configuration", "hybrid", None))
        self.editGoogle2Maptype.setItemText(1, _translate("Configuration", "satellite", None))
        self.editGoogle2Maptype.setItemText(2, _translate("Configuration", "roadmap", None))
        self.editGoogle2Maptype.setItemText(3, _translate("Configuration", "terrain", None))

