from finalscript import rasterprocess
import arcpy
import os

# inRasterWS = r"E:\Term3\GEOG-503\Final\testData\DEM"
# outputWS = r'E:\Term3\GEOG-503\Final\testData\Raster'
inRasterWS = arcpy.GetParameterAsText(0)
outputWS = arcpy.GetParameterAsText(1)
arcpy.CreateFolder_management(os.path.split(outputWS)[0], os.path.split(outputWS)[1])
parameter = [inRasterWS, outputWS]
rasterprocess.DEMtoRas(parameter)

