from finalscript import rasterprocess
import arcpy
import os

# inRasterWS = r"E:\Term3\GEOG-503\Final\testData\Raster"
# OutputWS = r'E:\Term3\GEOG-503\Final\testData\result'
# OutRaster = 'selectedDEM.tif'
inRasterWS = arcpy.GetParameterAsText(0)
outPut = arcpy.GetParameterAsText(1)


OutputWS = os.path.split(outPut)[0]
OutRaster = os.path.split(outPut)[1]
arcpy.AddMessage(OutputWS)

parameter = [inRasterWS, OutputWS, OutRaster]
rasterprocess.RasMosaic(parameter)
