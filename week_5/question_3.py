import numpy as np
import math
years, lattitudes,longitudes, depths, magnitudes = np.loadtxt('quake_data.txt').T #Transposed for easier unpacking
start_lon = -150
end_lon = -75
num_events = 0
lon_array = []
lat_array = []
for i in range(len(years)):
    if((longitudes[i] >= start_lon) and (longitudes[i] <= end_lon) ):
    	lon_array.append(longitudes[i])
	lat_array.append(lattitudes[i])
	num_events = num_events +1

np.savetxt('lat75to150.txt', lat_array)
np.savetxt('lon75to150.txt', lon_array)
print num_events
print lon_array
