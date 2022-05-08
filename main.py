"""
Run Bounding Box Code
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import pickle
import matplotlib.patches as patches
from boundingBox import boundingBox, multipleBox

file_handle = open("large_1_112_img.pkl", 'rb')
radar_data = pickle.load(file_handle)
length, width = np.shape(radar_data)
reflectivity_barrier = 60000

# box = boundingBox(radar_data)
# box.findEdges(reflectivity_barrier)
# print(box.center())
# box.plotBoundingBox()

multiplebox = multipleBox(radar_data)
multiplebox.grayScale(40000)