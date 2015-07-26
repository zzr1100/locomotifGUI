# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:47:55 2015

@author: Mirko
"""
import os

# this does not work in  the console
os.chdir(os.path.dirname(__file__))
# this is for the console, comment if script is run
# os.chdir("C:/Users/Mirko/SkyDrive/python/locomotifGUI")
os.chdir("C:/User/thomas.sonstiges/GitHub/locomotifGUI")


# After a UI file was created using QtDesigner, this has to be translated into
# a python class. The PyQt4 modules has a uic submodule for compiling ui files.
from PyQt4 import uic
uic.compileUiDir("ui/")
# please save all ui files prefixed by Ui_, then all python classes will also 
# be prefixed by ui. these classes only create the window and another class
# located in the project root, not prefixed by ui can inherit this class in 
# order to draw the correct window.
uic.compileUiDir("tools/")
