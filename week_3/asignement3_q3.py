import numpy as np

storm_id, pressure = np.loadtxt('minimalPressure.txt').T #Transposed for easier unpacking

final_id = []
min_pressure_array  = []
curr_id = storm_id[0]
curr_min_pressure = pressure[0]
for i in range(len(storm_id)):
    if(curr_id == storm_id[i]):
        if(curr_min_pressure > pressure[i]):
	    curr_min_pressure = pressure[i]
    else:
	curr_id = storm_id[i]
        final_id.append(storm_id[i-1])
        min_pressure_array.append(curr_min_pressure)
        curr_min_pressure = pressure[i]

print final_id
print " "
print min_pressure_array
print " "

np.savetxt('minpresures.txt', min_pressure_array)
np.savetxt('hurr_id_minpressures.txt', final_id)




