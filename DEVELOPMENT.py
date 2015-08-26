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
uic.compileUiDir("data/")
uic.compileUiDir("work/")
uic.compileUiDir("config/")
uic.compileUiDir("polyline/")
uic.compileUiDir("uicustom/")

#-----------------------------------------------------------------------------
# locomotif API 
#-----------------------------------------------------------------------------

# es gibt verschiedene vordefinierte Vormate, die von locomitf einfach eingelesen
# werden können. hierfür sind die konfigurationen jeweils in einer Datei hinterlegt.
# unter angabe der Versionsnummer der verwendet GPS gerätes, werden diese Einstellungen
# von locomitf direkt geladen. 
# die funktion gibt die daten als richtig formattierten pandas.DataFrame zurück.
import locomotif as loc
df = loc.read_csv('C:/user/thomas.sonstiges/GitHub/sample_data/schlossberg.txt', mapsta_version=100)

# diese Versionsnummer sollte nicht vom Nutzer abgerfragt werden, sondern über die Einstllungen dauerhaft
# festgelegt werden können. Zusätlich sollte es im Menu einen 'import txt' punkt geben, über den ein 
# dialog gestartet wird, in dem wie gewohnt spalten namen definiert und der separator festgelegt werden kann,
# z.b:

########## df = loc.read_csv('C:/user/thomas.sonstiges/GitHub/sample_data/schlossberg.txt', sep=";", header=True, usecols=['LAT', 'LON', 'SAT', 'HDOP', 'BIO', 'DIV'], names=['', '', 'lat', 'lon', 'biomass', 'diversity'])
# hier wird das format explizit angegeben, der header verwendet, die spalten angegeben die verwendet werden sollen und alle spalten umbenannt.
# wichtig für locomotif ist, dass df eine spalte 'lon' und 'lat' hat.


# das interne Objebt, das die Daten in locomotif verwaltet heißt Cluster und benötigt den obigen df.
c = loc.Cluster(df)
# das ding hat viele Methoden und bekommt noch mehr. z.B. kann sich ein CLuster auch auf die Platte speichern
# und mit loc.read_Cluster wieder geladen werden. Das wird in locomotifGUI die 'Projekte' sein.
# auf die daten im Cluster kann mittels den gegeben variablen namen zugegriffen werden
#c.biomass  # für names=['biomass']
#c.diversity # für diversity

# alle datasets in einem dictionary bekommt man mit c.getDatasets()
# return: {'biomass':c.biomass, 'diversity':c.diversity}
# könnte man verwenden um alle verfügbaren variablen abzufragen:
# vars = c.getDatasets().keys()
vars = c.getDatasets()

# zur berechnung gibt es momentan zwei funktionen, delaunay und voronoi,
# beide liefern das ergebnis is einem df zurück sowie das verwendete koordinatensystem
res11, ref = c.voronoi('biomass') # berechnet die voronoi polygone für biomass
res12, ref = c.voronoi('diversity') # berechnet die voronoi polygone für diversity
res21, ref = c.delaunay('biomass') # berechnet die delaunay polygone für biomass
res22, ref = c.delaunay('diversity') # berechnet die delaunay polygone für diversity
# ref kann überschrieben werden, da beide WGS84 verwenden (in den beispieldaten)

# danach können die interpolierten werte beider variablen mittels eines models 
# räumlich verrechnet werden. Dazu kommen noch beispiele. hierzu fehlt noch eine
# funktion um res1 und res2 in c zu integrieren (idealerweise ohne einen Namen vom User abzufragen...)

# datenausgabe:
# die df in res1, res2 aber auch c.biomass und c.diversity können als Shapefile 
# exportiert werden:
# loc.exportShp(res11, 'C:/user/thomas.sonstiges/GitHub/results/result_1.shp', SpatialReference=ref)
# loc.exportShp(res12, 'C:/user/thomas.sonstiges/GitHub/results/result_2.shp', SpatialReference=ref)
# diese funktion richtet allerdings noch ein mittelschweren chaos mit neuen ordnern an, die 
# muss noch debuggt werden.

# oder es kann eine Karte angefertigt werden:
# hierfür gibt es das Mapper Object. das kann entwerder initialisiert und dann 
# nach und nach die functionen aufgerufen werden, oder es wird alles notwendige übergeben
# und der Mapper erzeugt direkt die Karte:
# hierfür musst du mapnik installieren, was leider nicht ganz einfach ist und nur als 32bit version verfügbar
loc.Mapper(Style='Voronoi_index', size=(1920, 1024), datasource=res11, out_path="C:/user/thomas.sonstiges/GitHub/results/map11_v.png")
loc.Mapper(Style='Voronoi_index', size=(1920, 1024), datasource=res12, out_path="C:/user/thomas.sonstiges/GitHub/results/map12_V.png")
loc.Mapper(Style='Voronoi_index', size=(1920, 1024), datasource=res21, out_path="C:/user/thomas.sonstiges/GitHub/results/map21_V.png")
loc.Mapper(Style='Voronoi_index', size=(1920, 1024), datasource=res22, out_path="C:/user/thomas.sonstiges/GitHub/results/map22_V.png")
loc.Mapper(Style='Default', size=(1920, 1024), datasource=res11, out_path="C:/user/thomas.sonstiges/GitHub/results/map11_d.png")
loc.Mapper(Style='Default', size=(1920, 1024), datasource=res12, out_path="C:/user/thomas.sonstiges/GitHub/results/map12_d.png")
loc.Mapper(Style='Default', size=(1920, 1024), datasource=res21, out_path="C:/user/thomas.sonstiges/GitHub/results/map21_d.png")
loc.Mapper(Style='Default', size=(1920, 1024), datasource=res22, out_path="C:/user/thomas.sonstiges/GitHub/results/map22_d.png")

# the style is a xml file defining the style of the map located in the locomitf.mapper.style folder, 
# if absolute path is given, a valid mapnik style XML will be loaded from this location
# datasource can be a df containing OGR geometries as 'geometry' column and values as 'value' column 
# like in res1, res2, c.biomass etc.
# datasource can also be an absolute path of a Shapefile like the one above.
# out_path is the absolute path and filename for the rendered map. valid file types are: png, jpg, svg, pdf 
# and ::memory:: to save map as File-Like_object in RAM
