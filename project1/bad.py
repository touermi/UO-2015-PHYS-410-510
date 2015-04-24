import Image

fo = open("moon.txt", "r+")
#for j in range(0, 10):
#    print str0
    # format the line
yx = []
byteArray = ""
position = 0
for j in range(0, 1124 - 1):
#for j in range(0, 2):
    yx.append([])
    for i in range(0, 1024 - 1):
    #for i in range(0, 2):
    	str0 = fo.readline()
#        print " printing string"
#        print str0

        str_pos = []
    	for n in range(0, len(str0) - 1):
    	    if str0[n] == ".":
		str_pos.append(n)
    	    if str0[n] != " " and str0[n-1] ==" ":
            	str_pos.append(n)
#    	print str_pos
#    	print len(str_pos)
#        print "line = ", (j) * (i+1) + i
#    	print " x =", str0[0:str_pos[0]]
#    	print " y = ", str0[str_pos[1]:str_pos[2]]
#    	print "value =", str0[str_pos[3]:str_pos[4]]
#    	print "conver str to int"
        if str_pos[3] == str_pos[4]:
    	    value = str0[str_pos[3]+1] 
        else:
    	    value = str0[str_pos[3]:(str_pos[4]+1)]
        if j * (i+1) + i >= 120:  
            byteArray = byteArray + value
#        print byteArray
        yx[j].append(value) 
#    	print "value =", value
fo.close() 

image = Image.frombytes("RGB", (300, 300), byteArray)
#image = Image.fromarray(yx, "RGB")
image.show()
image.save("test.png")
#print yx
#print byteArray
#image = Image.open(StringIO.StringIO(1024 * 1124)
#str_pos = []

