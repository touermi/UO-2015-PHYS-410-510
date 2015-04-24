import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

x,y,temp = np.loadtxt('moon.txt').T #Transposed for easier unpacking
nrows, ncols = 1024, 1124

# conversion to 2D array
grid = temp.reshape((nrows, ncols))
gridprint = grid[499:600:,499:600];
fl = open('gridprint.csv', 'w')
writer = csv.writer(fl)
writer.writerow([])
for values in gridprint:
    writer.writerow(values)
fl.close()
raw_plot = plt.imshow(grid, extent=(x.min(), x.max(), y.max(), y.min()), cmap=cm.gray)
#plt.size(300, 300)
plt.show(raw_plot)

# copy inital 2d array
paved = np.zeros((1024, 1124))
for i in range(1024):
    for j in range(1124):
	paved[i, j] = grid[i, j]

# region that will be paved
paved[362:662, 412:712] = 0

paved_plot = plt.imshow(paved, extent=(x.min(), x.max(), y.max(), y.min()), cmap=cm.gray)
plt.show(paved_plot)

# array to hold the somthed data
smoth_array = np.zeros((1024, 1124))


# averaging funtion
def somthe_function(array):
    average = (np.sum(array)) / 25
    return average

for i in range(1024):
    for j in range(1124):
    	if i < 3 or i > 1020 or j < 3 or j > 1120 :
	    smoth_array[i, j] = grid[i, j]
	else: 
	    smoth_array[i, j] = somthe_function(grid[i:i+5, j:j+5])

average_plot = plt.imshow(smoth_array, extent=(x.min(), x.max(), y.max(), y.min()), cmap=cm.gray)
plt.show(average_plot)


#weighted smoth array
wsmoth_array = np.zeros((1024, 1124))
weight_array = np.array([[1/16., 2/16., 1/16.], [2/16., 4/16., 2/16.], [1/16., 2/16., 1/16.]], float)  

def weighted_smothe_function(array):
    sum_weigthed_average = np.sum(array * weight_array)
    return sum_weigthed_average

# applying weighet smothing 
for i in range(1024):
    for j in range(1124):
    	if i < 2 or i > 1021 or j < 2 or j > 1121 :
	    wsmoth_array[i, j] = grid[i, j]
	else: 
	    wsmoth_array[i, j] = weighted_smothe_function(grid[i:i+3, j:j+3])

weighted_plot = plt.imshow(wsmoth_array, extent=(x.min(), x.max(), y.max(), y.min()), cmap=cm.gray)
plt.show(weighted_plot)


# laplatian weighted smothing
lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], float)                  
lapsmothe_array = np.zeros((1024,1124))
def lap_smothe_function(array):
    #larray = array*lap
    sumlarray = np.sum(array * lap)
    return sumlarray

for i in range(1024):
    for j in range(1124):
        if i < 2 or i > 1021 or j < 2 or j > 1121:
            lapsmothe_array[i,j]=grid[i,j]
        else:
            lapsmothe_array[i,j]=lap_smothe_function(grid[i:i+3:,j:j+3:])                                                             
lap_plot = plt.imshow(grid-lapsmothe_array, extent=(x.min(), x.max(), y.max(), y.min()), cmap=cm.gray)

plt.show(lap_plot)                                                                                               
