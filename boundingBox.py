
import math
import matplotlib.pyplot as plt
import numpy as np
import pickle
import matplotlib.patches as patches

class boundingBox:
    x_min = None
    x_max = None
    y_min = None
    y_max = None
    num_pixels = None
    
    def __init__(self, radar_data):
        self.length, self.width = np.shape(radar_data)
        self.radar_data = radar_data

    def findEdges(self, reflectivity_barrier):
        high_reflectivity = []
        for i in range(self.length):
            for j in range(self.width):
                if(np.abs(self.radar_data[i][j])>reflectivity_barrier):
                    high_reflectivity.append((j,i))
        high_reflectivity = np.array(high_reflectivity)
        self.num_pixels, y = np.shape(high_reflectivity)
        minimums = np.amin(high_reflectivity, axis = 0)
        self.x_min = minimums[0]
        self.y_min = minimums[1]
        maximums = np.amax(high_reflectivity, axis = 0)
        self.x_max = maximums[0]
        self.y_max = maximums[1]
        return self.x_min, self.y_min, self.x_max, self.y_max

    def center(self):
        return ((self.x_min+self.x_max)/2, (self.y_min+self.y_max)/2)
    
    def plotBoundingBox(self):
        plt.imshow(abs(self.radar_data))
        figure, ax = plt.subplots(1)
        rect = patches.Rectangle((self.x_min, self.y_min), self.x_max-self.x_min, self.y_max-self.y_min, linewidth=1, fill=False)
        ax.imshow(abs(self.radar_data))
        ax.add_patch(rect)
        plt.show()

class multipleBox:
    centers = []
    def __init__(self, radar_data):
        self.length, self.width = np.shape(radar_data)
        self.radar_data = radar_data
    def grayScale(self, reflectivity_barrier):
        grayMap = np.abs(self.radar_data)
        grayMap[grayMap > reflectivity_barrier] = 1
        grayMap[grayMap != 1] = 0
        for i in range(1, self.length-1):
            for j in range(1, self.width-1):
                if grayMap[i][j]==0 and ([grayMap[i-1][j]==1, grayMap[i+1][j]==1, grayMap[i][j-1]==1, grayMap[i][j+1]==1].count(True) >= 2):
                    grayMap[i][j]=1
                    print("converted to 1")
                if grayMap[i][j]==1 and ([grayMap[i-1][j]==0, grayMap[i+1][j]==0, grayMap[i][j-1]==0, grayMap[i][j+1]==0].count(True) >= 3):
                    grayMap[i][j]=0
                    print("converted to 0")
        plt.imshow(grayMap, cmap='Greys')
        plt.show()
