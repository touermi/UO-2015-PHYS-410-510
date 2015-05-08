import numpy as np
import math
years,lattitudes,longitudes, depths, magnitudes = np.loadtxt('quake_data.txt').T #Transposed for easier unpacking
longitude_user = (input('Enter the longitude = '))
print longitude_user
lattitude_user = (input('Enter the lattitude = '))
start_year = int(input('Enter start year = '))
end_year = int(input('Enter end year ='))
num_events = 0
for i in range(len(years)):

    if((longitudes[i] <= longitude_user +1) and (longitudes[i] >= longitude_user -1) ):
        print "before lat" 
        if((lattitudes[i] <= lattitude_user +1) and (lattitudes[i] >= lattitude_user -1) ):
            print "before years" 
    	    if((years[i] <= end_year) and years[i] >= start_year):
		num_events = num_events +1
		print num_events
#seattle location
seattle_long = -122.3331
seattle_lat = 47.6097
seattle_earthquakes_perdecade = []
curr_year = years[0]
num_earthquakes_inseattle = 0
pi = math.acos(-1)

#  This function to calculate distance
def distance(long1, lat1, long2, lat2):
    theta = long1 - long2
    dist = math.sin(lat1 * pi/180) * math.sin(lat2 * pi/180) +  math.cos(lat1 * pi/180) * math.cos(lat2 * pi/180) * math.cos(theta * pi/180) 
    dist = math.acos(dist)
    dist = dist *180/pi
    dist = dist * 60 * 1.1515
    return dist
for i in range(len(years)):
     if((years[i] >= curr_year) and (years[i] < curr_year + 10)):
     	if( distance(seattle_long, seattle_lat, longitudes[i], lattitudes[i]) <= 1000):
            num_earthquakes_inseattle = num_earthquakes_inseattle + 1
     else:
     	if( distance(seattle_long, seattle_lat, longitudes[i], lattitudes[i]) <= 1000):
	    seattle_earthquakes_perdecade.append(num_earthquakes_inseattle)
            num_earthquakes_inseattle = 1
            curr_year = curr_year + 10
        else:
	    seattle_earthquakes_perdecade.append(num_earthquakes_inseattle)
            num_earthquakes_inseattle = 0
            curr_year = curr_year + 10

print seattle_earthquakes_perdecade
np.savetxt('seattlequakes.txt', seattle_earthquakes_perdecade)
print num_events


