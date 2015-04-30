import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x,y,lum = np.loadtxt('stars.txt').T
nrows, ncols = 1024, 1124
framed = lum.reshape((nrows, ncols))

starspic = plt.imshow(framed, extent=(x.min(), x.max(), y.max(), y.min()),
           interpolation='nearest', cmap=cm.gray)
plt.show(starspic)


filt = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
mask = np.zeros((1024,1124))

def maxer(array):
    value = array*filt
    sumint = np.sum(value)
    avg = sumint/25
    return avg

xlist = []
ylist = []

for i in range(1024):
    for j in range(1124):
        if i<1 or i>1018 or j<1 or j>1118:
            pass
        elif maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i-1:i+4:,j-1:j+4:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i:i+5:,j-1:j+4:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i+1:i+6:,j-1:j+4:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i-1:i+4:,j:j+5:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i+1:i+6:,j:j+5:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i-1:i+4:,j+1:j+6:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i:i+5:,j+1:j+6:]) and \
             maxer(framed[i:i+5:,j:j+5:])>maxer(framed[i+1:i+6:,j+1:j+6:]) and \
             np.sum(maxer(framed[i:i+5:,j:j+5:]))>12000:
                mask[i,j]=10000
                xlist.append(i)
                ylist.append(j)

maskpic = plt.imshow(mask, extent=(x.min(), x.max(), y.max(), y.min()),
           interpolation='nearest', cmap=cm.gray)
print len(xlist)        
plt.show(maskpic)

print np.shape(xlist)
print np.shape(ylist)


