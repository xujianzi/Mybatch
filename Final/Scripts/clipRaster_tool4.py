from finalscript import rasterprocess
import arcpy
import os

# inputRas = r"E:\Term3\GEOG-503\Final\testData\result\selectedDEM.tif"
# inputShp = r'E:\Term3\GEOG-503\Final\testData\shapefile\Selected.shp'
# outRaster = r'E:\Term3\GEOG-503\Final\testData\result\test.tif'
# ws = r'E:\Term3\GEOG-503\Final\testData\result'
inputRas = arcpy.GetParameterAsText(0)
inputShp = arcpy.GetParameterAsText(1)
outRaster = arcpy.GetParameterAsText(2)
ws = os.path.split(outRaster)[0]

parameter = [inputRas, inputShp, outRaster, ws]
rasterprocess.ClipRasters(parameter)
