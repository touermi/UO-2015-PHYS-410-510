import numpy as np
import math
data = np.loadtxt('columnD.txt').T #Transposed for easier unpacking
years = np.loadtxt('columnC.txt').T #Transposed for easier unpacking

curr_y = years[0]
temp_array = []

av_array = []
std_array = []
y_array = []

for i in range(len(data)):
    if((years[i] < curr_y + 10) and (years[i] >= curr_y)):
	temp_array.append(data[i])
    else:	
        av = np.sum(temp_array)/(len(temp_array) )
        temp = 0
        for j in range(len(temp_array)):
            temp  = (temp_array[j] - av) * (temp_array[j] - av) + temp
            std = temp / (len(temp_array) - 1)
        y_array.append(curr_y)
        av_array.append(av)
        std_array.append(std)
        temp_array = []
        temp_array.append(data[i])
        curr_y = years[i]
        
print "The average is =", av_array

print "the sdt is = ", std_array


np.savetxt('averages.txt', av_array)
np.savetxt('stds.txt', std_array)
np.savetxt('years.txt', y_array)

