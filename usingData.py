
import math
import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

file_handle = open("large_1_112_img.pkl", 'rb')

radar_data = pickle.load(file_handle)

# x = radar_data.real
# # extract imaginary part using numpy array
# y = radar_data.imag
  
# # plot the complex numbers
# plt.plot(x, y, 'g*')
# plt.ylabel('Imaginary')
# plt.xlabel('Real')
# plt.show()

#plt.imshow(np.abs(radar_data))
plt.show(np.abs(radar_data))
plt.savefig('image.jpg')