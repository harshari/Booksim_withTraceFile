import math
import numpy as np
import collections


outfile = open("./trace" + ".txt", "w")

'''
###K,Q,V

counter=0
for i in range(0,256):
    for j in range(0,4):
        outfile.write(str(j)  + " " + str(j*4+6+(counter%4)) + " " + str(i) + "\n")
    counter+=1

counter=0
for i in range(256,384):
    for j in range(0,4):
        outfile.write(str(j*4+6+(counter%4))+ " " + str(j) + " " + str(i) + "\n")
    counter+=1

outfile.write("\n")
outfile.close()



###Score

outfile = open("./trace" + ".txt", "w")

counter=0
for i in range(0,256):
    for j in range(0,2):
        outfile.write(str(j+4)  + " " + str(21+j*3+(counter%3)) + " " + str(i) + "\n")
    counter+=1

counter=0
for i in range(256,384):
    for j in range(0,2):
        outfile.write(str(21+j*3+(counter%3))+ " " + str(j+4) + " " + str(i) + "\n")
    counter+=1

outfile.write("\n")
outfile.close()

'''
'''
###ReRAM

outfile = open("./trace" + ".txt", "w")

counter=0
for i in range(0,256):
    for j in range(0,2):
        outfile.write(str(j+4)  + " " + str(21+j*3+(counter%3)) + " " + str(i) + "\n")
    counter+=1

counter=0
for i in range(256,384):
    for j in range(0,2):
        outfile.write(str(21+j*3+(counter%3))+ " " + str(j+4) + " " + str(i) + "\n")
    counter+=1

outfile.write("\n")
outfile.close()



###ReRAM

outfile = open("./trace" + ".txt", "w")

counter=0
for i in range(0,49):
    for j in range(0,8):
        outfile.write(str(j)  + " " + str(j+1) + " " + str(i) + "\n")
    counter+=1


outfile.write("\n")
outfile.close()
'''

'''
###TransPIM

outfile = open("./trace" + ".txt", "w")

for i in range(0,16):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str((j+1)%8) + " " + str(i) + "\n")


for i in range(16,32):
    for j in range(8,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(32,48):
    for j in range(16,24):
        outfile.write(str(j)+ " " + str((j+1)%24) + " " + str(i) + "\n")


outfile.write("\n")
outfile.close()
'''

'''

###TransPIM

outfile = open("./trace" + ".txt", "w")

for i in range(0,16):
    for j in range(16,24):
        outfile.write(str(j)+ " " + str((j+1)%24) + " " + str(i) + "\n")


outfile.write("\n")
outfile.close()

'''

'''
###TransPIM

outfile = open("./trace" + ".txt", "w")

counter=0
for i in range(0,36):
    for j in range(0,16):
        outfile.write(str(i)+ " " + str((i+1)%36) + " " + str(j+16*counter) + "\n")
    counter+=1

outfile.write("\n")
outfile.close()

'''
'''
outfile = open("./trace" + ".txt", "w")

for i in range(0,16):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str((j+1)%8) + " " + str(i) + "\n")


for i in range(16,32):
    for j in range(8,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(32,48):
    for j in range(16,24):
        outfile.write(str(j)+ " " + str((j+1)%24) + " " + str(i) + "\n")

counter=0
for i in range(0,16):
    for j in range(0,35):
        outfile.write("36" + " " + str(j) + " " + str(counter*36+ 48+j) + "\n")
    counter+=1



outfile.write("\n")
outfile.close()

'''
'''
outfile = open("./trace" + ".txt", "w")


counter=0
for i in range(0,32):
    for j in range(0,35):
        outfile.write("36" + " " + str(j) + " " + str(counter*36 +j) + "\n")
    counter+=1



outfile.write("\n")
outfile.close()

'''

'''
###HAIMA

outfile = open("./trace" + ".txt", "w")

for i in range(0,8):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str((j+1)%8) + " " + str(i) + "\n")


for i in range(8,16):
    for j in range(8,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(16,24):
    for j in range(16,24):
        outfile.write(str(j)+ " " + str((j+1)%24) + " " + str(i) + "\n")


outfile.write("\n")
outfile.close()
'''

'''

###HAIMA

outfile = open("./trace" + ".txt", "w")

for i in range(0,8):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str((j+1)%8) + " " + str(i) + "\n")
    

counter=0
for i in range(8,64):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str(29) + " " + str(counter*8 +i) + "\n")
    counter+=1 

for i in range(504,512):
    for j in range(8,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")

counter=0
for i in range(512,568):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str(30) + " " + str(counter*8 +i) + "\n")
    counter+=1 

for i in range(1008,1016):
    for j in range(8,16):
        outfile.write(str(j)+ " " + str((j+1)%24) + " " + str(i) + "\n")

counter=0
for i in range(1016,1072):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str(31) + " " + str(counter*8 +i) + "\n")
    counter+=1 

outfile.write("\n")
outfile.close()

'''

'''
###HAIMA

outfile = open("./trace" + ".txt", "w")

for i in range(0,16):
    for j in range(0,8):
        outfile.write(str(j)+ " " + str((j+1)%8) + " " + str(i) + "\n")


for i in range(16,32):
    for j in range(8,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(32,48):
    for j in range(16,24):
        outfile.write(str(j)+ " " + str((j+1)%24) + " " + str(i) + "\n")

counter=0
for i in range(0,16):
    for j in range(0,35):
        outfile.write("36" + " " + str(j) + " " + str(counter*36+ 48+j) + "\n")
    counter+=1


outfile.write("\n")
outfile.close()
'''



outfile = open("./trace" + ".txt", "w")


counter=0
for i in range(0,32):
    for j in range(0,35):
        outfile.write("36" + " " + str(j) + " " + str(counter*36 +j) + "\n")
    counter+=1



outfile.write("\n")
outfile.close()