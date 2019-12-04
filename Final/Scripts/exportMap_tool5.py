from finalscript import mapexport
import arcpy


# inMap = r'E:\Term3\GEOG-503\Final\final.mxd'
# outMap = r'E:\Term3\GEOG-503\Final\testData\result\test.jpg'
# '''Please change the directory of inMap and outJPEG to your test data folder'''
inMap = arcpy.GetParameterAsText(0)
outMap = arcpy.GetParameterAsText(1)
formatMap = arcpy.GetParameterAsText(2)
arcpy.AddMessage(formatMap)
parameter = [inMap, outMap, formatMap]
mapexport.exportMap(parameter)
