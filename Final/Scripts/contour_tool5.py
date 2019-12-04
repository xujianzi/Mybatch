from finalscript import rasterprocess
import arcpy
import os


# inputRas = r"E:\Term3\GEOG-503\Final\testData\result\selectedDEM.tif"
# interval = 200
# base = 0
# output = r'E:\Term3\GEOG-503\Final\testData\result\contour.shp'
inputRas = arcpy.GetParameterAsText(0)
interval = int(arcpy.GetParameterAsText(1))
base = int(arcpy.GetParameterAsText(2))
output = arcpy.GetParameterAsText(3)
parameter = [inputRas, interval, base, output]
rasterprocess.GenContour(parameter)
