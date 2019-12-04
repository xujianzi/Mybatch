# -*- coding:utf-8 -*-
__author__ = 'Jian Xu'

import arcpy
import os
arcpy.env.overwriteOutput = True


# Batch Clip function
def MyBatchClip(Parameter):
    # parameter
    inputFC = Parameter[0]
    ClipArea = Parameter[1]
    OutputWS = Parameter[2]
    Fields = ['FID', 'SHAPE@', 'NAME10']
    with arcpy.da.SearchCursor(ClipArea,Fields) as cursor:
        for row in cursor:
            outputFC = os.path.join(OutputWS, str(row[2]) + '_' + str(row[0]) + '.shp')
            arcpy.Clip_analysis(inputFC, row[1], outputFC)
            print(str(row[2]) + '_' + str(row[0]) + '.shp')

