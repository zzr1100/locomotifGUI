# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Mirko
"""
import sys
from PyQt4 import QtGui, QtCore
from ui.Ui_Locomotif import Ui_Locomotif

class Locomotif(QtGui.QMainWindow):
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
        self.ui = Ui_Locomotif()
        # Ui_Locomotif knows setupUi and retranslateUi methods
        self.ui.setupUi(self)







if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Locomotif()
    myapp.show()
    sys.exit(app.exec_())