import numpy as np
import math
years, lattitudes,longitudes, depths, magnitudes = np.loadtxt('quake_data.txt').T #Transposed for easier unpacking
start_lon = -150
end_lon = -75
num_events = 0
lon_array = []
lat_array = []
year_array = []
mag_array = []
for i in range(len(years)):
    if(magnitudes[i] > 7.00):
    	lon_array.append(longitudes[i])
	lat_array.append(lattitudes[i])
        mag_array.append(magnitudes[i])
        year_array.append(years[i])
	num_events = num_events +1
np.savetxt('lon_above7.txt', lon_array)
np.savetxt('lat_above7.txt', lat_array)
np.savetxt('mag_above7.txt', mag_array)
curr_year = year_array[0]
count = 0
y_array = []
event_array = []
for i in range(len(lat_array)):
    if(year_array[i] == curr_year):
        count = count + 1
    else:
        event_array.append(count)
        y_array.append(curr_year)
        count = 1
        curr_year = year_array[i]

np.savetxt('yearsevents.txt', y_array)
np.savetxt('numbperyear.txt', event_array)
	
