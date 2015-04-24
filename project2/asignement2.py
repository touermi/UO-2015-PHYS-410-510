# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv
import math
import argparse
import cv2

x,y,temp = np.loadtxt('galaxy.txt').T #Transposed for easier unpacking
stars = []

for p in range(1124 * 1024):
    if temp[p] > 5000:
	stars.append(p)
print len(stars)
starsList= [[0]]
#print stars[0]
#starsList = starsList.append(stars[0])
stars.remove(stars[0])
print len(stars)
print starsList
m = 5
#while(len(stars) > 0):
for a in range(len(stars)):
    is_appended = 1
    for j  in range(len(starsList)):
        for l in range(len(starsList[j])):
            k = starsList[j][l]
  	    i = stars[a]			      
            if((x[i] < 1020) and (x[i] > 1) and (y[i] < 1120) and (y[i] > 1)):
            	if( (x[i] == x[k]-1) and (y[i] == y[k]-1)) or ( (x[i] == x[k]+1) and (y[i] == y[k]-1)) or ( (x[i] == x[k]-1) and (y[i] == y[k]+1)) or ( (x[i] == x[k]+1) and (y[i] == y[k]+1) ) or ( (x[i] == x[k]-0)  and (y[i] == y[k]-1)) or ((x[i] == x[k]-1) and (y[i] == y[k]-0)) or ((x[i] == x[k]+0) and (y[i] == y[k]+1)) or ((x[i] == x[k]+1) and (y[i] == y[k]+0)): 
                    #print 'I am neighberjhood'
		    starsList[j].append(i)
                    #stars.remove(i)
                    is_appended = - 1
                    break
	if((j == len(starsList)-1) and (is_appended != -1) ):
            #print 'I am at teh end'
	    starsList.append([stars[a]])
            is_appended = -1
            #stars.remove([i])
            break
        if(is_appended == -1):
	    break
print starsList
print len(starsList)
xsum = 0
ysum = 0
zsum = 0
data = []
xlist = []
ylist = []
list = []
for l in range(len(starsList)):
    for k in range(len(starsList[l])):
	i = starsList[l][k] 
        xsum = xsum + x[i]
        ysum = ysum + y[i]
        zsum = zsum + temp[i]
    xlist.append( math.ceil(xsum / len(starsList[l])) )
    ylist.append( math.ceil(ysum / len(starsList[l])) )
    zlist.append( math.ceil(zsum / len(starsList[l])) )
    data.append([ math.ceil(xsum / len(starsList[l])),  math.ceil(ysum / len(starsList[l])),  math.ceil(zsum / len(starsList[l])) ])
np.savetxt('testx.txt', xlist)
np.savetxt('testy.txt', ylist)
np.savetxt('testz.txt', zlist)
print xlist
print len(xlist)

           

'''
list_of_stars = []
t = [1]
r= [2, 3]
list_of_stars.append(t)
print list_of_stars
list_of_stars.append(r)

print list_of_stars
print len(list_of_stars)
list_of_stars[0].append(0)
print list_of_stars[0]
print len(list_of_stars)
'''
'''
for i in range(1124 * 1024):

    j = 0
    n = len(stars)
    if(n == 0 and temp[i] > 7000):
        startList = [i]
        stars.append(startList)
    while j < n :
        m = len( stars[j])
        k = 0
     	while k < m:
            if temp[i] > 700:
                print i
		if(x(i) == x(k)) and (y(i) == y(k)):
		     k = m+5
                     j = n + 5
                elif ( (x[i] == x[k]-1) and (y[i] == y[k]-1)) or ( (x[i] == x[k]+1) and (y[i] == y[k]-1)) or ( (x[i] == x[k]-1) and (y[i] == y[k]+1)) or ( (x[i] == x[k]+1) and (y[i] == y[k]+1) ) or ( (x[i] == x[k]-0)  and (y[i] == y[k]-1)) or ((x[i] == x[k]-1) and (y[i] == y[k]-0)) or ((x(i) == x[k]+0) and (y[i] == y[k]+1)) or ((x[i] == x[k]+1) and (y[i] == y[k]+0)): 

		    stars[j].append(i)
                    print 'updating star element', i, ',', j, '=',stars((i, j))
                    break
                    m = m + 1
                    k = m + 5
                    j = n + 5
                elif k == m-1 and j == n - 1:
                    newList = [i]
		    stars.append(newList)
                    break
                elif k == m -1 and j < n-1:
                    n = n+1  
                else :
                    k = k +1
      j = j + 1
print len(stars)
for i in range(len(stars)):
    print len(stars[i])
'''
'''
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
raw_plot = plt.imshow(grid, cmap=cm.gray)
#plt.show(raw_plot)
plt.savefig('foo.png')

im = cv2.imread('foo.png')
hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
COLOR_MIN = np.array([20, 20, 20],np.uint8)
COLOR_MAX = np.array([0, 0, 0],np.uint8)
frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)
imgray = frame_threshed
ret,thresh = cv2.threshold(frame_threshed,127,255,0)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[0]
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Show",im)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
im = cv2.imread('foo.png')
hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
COLOR_MIN = np.array(0,np.uint8)
COLOR_MAX = np.array(20,np.uint8)
frame_threshed = cv2.inRange( int(temp/temp.max() * 255), COLOR_MIN, COLOR_MAX)
imgray = frame_threshed
ret,thresh = cv2.threshold(frame_threshed,127,255,0)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[0]
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Show",im)
cv2.waitKey()
cv2.destroyAllWindows()

                                    '''                                                  
