import arcpy
import os

arcpy.env.overwriteOutput = True


def DEMtoRas(parameter):

    inputWS = parameter[0]
    outputWS = parameter[1]
    arcpy.env.workspace = inputWS
    arcpy.CheckOutExtension("Spatial")
    for ras in arcpy.ListRasters():
        print(ras)
        arcpy.AddMessage(ras)
        inputDEM = os.path.join(inputWS, ras)
        arcpy.DEMToRaster_conversion(inputDEM, os.path.join(outputWS, str(ras)+'.tif'))
    arcpy.CheckInExtension("Spatial")

def RasMosaic(parameter):
    inputWS = parameter[0]
    outputWS = parameter[1]
    output = parameter[2]
    arcpy.env.workspace = inputWS
    arcpy.CheckOutExtension("Spatial")
    raster = arcpy.ListRasters()
    arcpy.MosaicToNewRaster_management(raster, outputWS, output, pixel_type="16_BIT_SIGNED", number_of_bands=1)
    arcpy.CheckInExtension("Spatial")

def ClipRasters(parameter):
    arcpy.env.overwriteOutput = True
    inputRas = parameter[0]
    clipFeature = parameter[1]
    output = parameter[2]
    ws = parameter[3]
    arcpy.env.workspace = ws
    arcpy.env.mask = clipFeature
    arcpy.CheckOutExtension("Spatial")
    dem = arcpy.sa.ExtractByMask(inputRas, clipFeature)
    dem.save(output)
    print(dem)
    arcpy.CheckInExtension("Spatial")

def GenContour(parameter):
    arcpy.env.overwriteOutput = True
    inputRas = parameter[0]
    interval = int(parameter[1])
    base = int(parameter[2])
    output = parameter[3]
    arcpy.CheckOutExtension("Spatial")
    arcpy.sa.Contour(inputRas, output, interval, base)
    arcpy.CheckInExtension("Spatial")