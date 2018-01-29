# Name: PointsToPolygon.py
# Description: 	Use PointsToLine to create lines from coordinates
#				& FeatureToPloygon function to construct polygon from ENCLOSED lines
# Author: Shubham Shirbhate

import arcpy
from arcpy import env

# Fill your Dropbox 'DroneETDatabase.mdb' file address
env.workspace = "E:\\Dropbox (UFL)\\DroneET(Shared)\\"

# FIRST, constructing lines from coordinates
# Hastings
arcpy.PointsToLine_management("DroneETDatabase.mdb\\Coordinates_Hastings", "DroneETDatabase.mdb\\OutLines_Hastings")

# Kempfer_SeepIrrigation
arcpy.PointsToLine_management("DroneETDatabase.mdb\\Coordinates_Kempfer_SeepIrrigation", "DroneETDatabase.mdb\\OutLines_Kempfer_SeepIrrigation")

# Kempfer_SubSurfaceIrrigation
arcpy.PointsToLine_management("DroneETDatabase.mdb\\Coordinates_Kempfer_SubSurfaceIrrigation", "DroneETDatabase.mdb\\OutLines_Kempfer_SubSurfaceIrrigation")


# SECOND, contructing polygon from the lines
#Hastings
arcpy.FeatureToPolygon_management("DroneETDatabase.mdb\\OutLines_Hastings", "DroneETDatabase.mdb\\Polygon_Hastings","","ATTRIBUTES","")

# Kempfer_SeepIrrigation
arcpy.FeatureToPolygon_management("DroneETDatabase.mdb\\OutLines_Kempfer_SeepIrrigation", "DroneETDatabase.mdb\\Polygon_Kempfer_SeepIrrigation","","ATTRIBUTES","")

# Kempfer_SubSurfaceIrrigation
arcpy.FeatureToPolygon_management("DroneETDatabase.mdb\\OutLines_Kempfer_SubSurfaceIrrigation", "DroneETDatabase.mdb\\Polygon_Kempfer_SubSurfaceIrrigation","","ATTRIBUTES","")







# GENERAL CODE
"""

# Import system modules
import arcpy

# Set local variables for Lines
inFeaturesLines = " ##FILL path for the input coordinates"
outFeaturesLines = " ##FILL path for the output lines"
lineField = ""
sortField = ""

# Set local parameters for Polygon
inFeaturesPolygon = [" ##FILL path for the output lines"]
outFeatureClassPolygon = " ##FILL path for the output polygon"
clusTol = ""


# Execute PointsToLine - Create lines from the coordinates 
arcpy.PointsToLine_management(inFeaturesLines, outFeaturesLines, lineField, sortField)


# Use the FeatureToPolygon function to form new areas from ECLOSED lines
arcpy.FeatureToPolygon_management(inFeaturesPolygon, outFeatureClassPolygon, clusTol,
                                  "ATTRIBUTES", "")

"""


# REFERENCE

# Points To Line (Data Management)
# http://resources.arcgis.com/en/help/main/10.1/index.html#//00170000003s000000

# Feature To Polygon (Data Management)
# http://resources.arcgis.com/en/help/main/10.1/index.html#/Feature_To_Polygon/00170000003n000000/