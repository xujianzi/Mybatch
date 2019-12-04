from arcpy import mapping
import arcpy

def exportMap(parameter):
    inMap = parameter[0]
    outMap = parameter[1]
    formatMap = parameter[2]
    arcpy.env.overwriteOutput = True
    mxd = mapping.MapDocument(inMap)
    mxd.activeView = 'PAGE_LAYOUT'
    if formatMap == 'JPEG':
        mapping.ExportToJPEG(mxd, outMap)
    if formatMap == 'PDF':
        mapping.ExportToPDF(mxd, outMap)
    if formatMap == 'BMP':
        mapping.ExportToBMP(mxd, outMap)
    if formatMap == 'PNG':
        mapping.ExportToPNG(mxd, outMap)
    if formatMap == 'TIFF':
        mapping.ExportToTIFF(mxd, outMap)
    if formatMap == 'GIF':
        mapping.ExportToGIF(mxd, outMap)
    else:
        mapping.ExportToJPEG(mxd, outMap)
