import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

stormID, data = np.loadtxt('Id_and_year.txt').T #Transposed for easier unpacking

years = []
numbHurr = []
curr_year = data[0]
curr_id = stormID[0]
tracker = 1


for i in range(len(data)):
    if(curr_year == data[i]):
        if( curr_id != stormID[i]):
            tracker = tracker + 1
            curr_id = stormID[i]
    else: 
	years.append(data[i - 1])
        numbHurr.append(tracker)
        tracker = 1
        curr_year = data[i]
        curr_id = stormID[i]

 
years.append(data[ len(data) - 1])
numbHurr.append(tracker)
np.savetxt('years.txt', years)
np.savetxt('numbHurr.txt', numbHurr)

print years
print numbHurr


                                                                                      
