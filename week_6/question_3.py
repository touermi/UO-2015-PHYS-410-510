import numpy as np
import matplotlib.pyplot as plt
import math
data = np.loadtxt('columnD.txt').T #Transposed for easier unpacking
years = np.loadtxt('columnC.txt').T #Transposed for easier unpacking

curr_y = years[0]
temp_array = []

av_array = []
std_array = []
y_array = []

for i in range(len(data) - 1):
    if(i == len(data) - 1):
        av = np.sum(temp_array)/(len(temp_array) )
        temp = 0
        for j in range(len(temp_array)):
            temp  = (temp_array[j] - av) * (temp_array[j] - av) + temp
            std = temp / (len(temp_array) - 1)
        y_array.append(curr_y)
        av_array.append(av)
        std_array.append(std)
        temp_array = []
 
    if((years[i] < curr_y + 10) and (years[i] >= curr_y)):
	temp_array.append(data[i])
    else:	
        av = np.sum(temp_array)/(len(temp_array) )
        temp = 0
        for j in range(len(temp_array) -1 ):
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
s_v_bar = []
e_v_bar = []
s_sbox = []
e_sbox = []
for i in range(len(y_array)):
     # change 2 with 1.5 as needed 
     s_v_bar.append(-2 * std_array[i] + av_array[i] - 0.05)
     e_v_bar.append(+2 * std_array[i] + av_array[i] + 0.05)
     s_sbox.append(av_array[i] - 0.05)
     e_sbox.append(av_array[i] + 0.05)

np.savetxt('averages.txt', av_array)
#np.savetxt('stds.txt', std_array)
#np.savetxt('years.txt', y_array)
#np.savetxt('s_v_bar.txt', s_v_bar)
#np.savetxt('e_v_bar.txt', e_v_bar)
#np.savetxt('s_sbox.txt', s_sbox)
#np.savetxt('e_sbox.txt', e_sbox)

b = open("avraw.txt", 'w')
for i in range(len(y_array)): 
   value = ['',y_array[i],'', s_v_bar[i], s_sbox[i], e_sbox[i], e_v_bar[i]],
   b.write(str(value) )
b.close()
         
 


######################################### last part of question 3#################
index = 0
k = 0
curr_year = years[0]
temp_1d = []
temp_2y = []
slope_array = []
p_year = []
while (k < len(data)):
    if(years[k]== curr_year + 10):
    	index = k
    if((years[k] < curr_year + 30) and (years[k] >= curr_year)):
        temp_1d.append(data[k])
        temp_2y.append(years[k])
	k = k + 1
    else:
	slope, intercept = np.polyfit(np.log(temp_1d), np.log(temp_2y), 1)
	print(slope)
        slope_array.append(slope)
        p_year.append(curr_year)
        temp_1d =[]
        temp_2y = []
        k = index
        curr_year = years[k]

print slope_array
#np.savetxt('slopes.txt', slope_array)

a = open("slopesraw.txt", 'w')
for i in range(len(slope_array)): 
   value0 = p_year[i]
   value1 = p_year[i]+30
   value3 = "",value0,'-',value1,""
   value = [value3, slope_array[i]],
   a.write(str(value) )
a.close()
         
    
