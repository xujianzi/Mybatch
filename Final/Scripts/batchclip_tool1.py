import time
from finalscript import shapeprocess
import arcpy
import os

# infeature = r'E:\Term3\GEOG-503\Final\testData\shapefile\NY_Counties.shp'
# clipArea = r'E:\Term3\GEOG-503\Final\testData\shapefile\NY_Counties.shp'
# outputWS = r'E:\Term3\GEOG-503\Final\testData\result\shapefile'
infeature = arcpy.GetParameterAsText(0)
clipArea = arcpy.GetParameterAsText(1)
outputWS = arcpy.GetParameterAsText(2)
arcpy.CreateFolder_management(os.path.split(outputWS)[0], os.path.split(outputWS)[1])
Parameter1 = [infeature, clipArea, outputWS]
StartTime = time.time()
shapeprocess.MyBatchClip(Parameter1)
EndTime = time.time()
# print 'Elapsed:  ' + str(EndTime - StartTime) + '  Seconds...'
arcpy.AddMessage('Elapsed:  ' + str(EndTime - StartTime) + '  Seconds...')


