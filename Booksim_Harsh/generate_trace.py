import math
import numpy as np
import collections

'''
outfile = open("./trace" + ".txt", "w")



outfile = open("./trace" + ".txt", "w")


counter=0
for i in range(0,96):
    for j in range(0,96):
        outfile.write("100" + " " + str(j) + " " + str(counter*96 +j) + "\n")
    counter+=1


outfile.write("\n")
outfile.close()
'''



'''
###TransPIM

outfile = open("./trace" + ".txt", "w")

for i in range(0,64):
    for j in range(0,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(64,128):
    for j in range(16,32):
        outfile.write(str(j)+ " " + str((j+1)%32) + " " + str(i) + "\n")

for i in range(128,192):
    for j in range(32,48):
        outfile.write(str(j)+ " " + str((j+1)%48) + " " + str(i) + "\n")

counter=0
for i in range(0,64):
    for j in range(0,96):
        outfile.write("100" + " " + str(j) + " " + str(counter*96+ 192+j) + "\n")
    counter+=1

outfile.write("\n")
outfile.close()

'''




'''
###HAIMA

outfile = open("./trace" + ".txt", "w")

for i in range(0,16):
    for j in range(0,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(16,32):
    for j in range(16,32):
        outfile.write(str(j)+ " " + str((j+1)%32) + " " + str(i) + "\n")


for i in range(32,48):
    for j in range(32,48):
        outfile.write(str(j)+ " " + str((j+1)%48) + " " + str(i) + "\n")


outfile.write("\n")
outfile.close()
'''



###HAIMA

outfile = open("./trace" + ".txt", "w")

for i in range(0,8):
    for j in range(0,16):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")
    

counter=0
for i in range(8,72):
    for j in range(0,16):
        outfile.write(str(j)+ " " + str(96) + " " + str(counter*16 + j+8) + "\n")
    counter+=1 

for i in range(1152,1160):
    for j in range(16,32):
        outfile.write(str(j)+ " " + str((j+1)%32) + " " + str(i) + "\n")

counter=0
for i in range(1160,1224):
    for j in range(16,32):
        outfile.write(str(j)+ " " + str(97) + " " + str(counter*16 + j+1160) + "\n")
    counter+=1 

for i in range(2200,2208):
    for j in range(32,48):
        outfile.write(str(j)+ " " + str((j+1)%48) + " " + str(i) + "\n")

counter=0
for i in range(2208,2272):
    for j in range(32,48):
        outfile.write(str(j)+ " " + str(98) + " " + str(counter*16 + j+2208) + "\n")
    counter+=1 


counter=0
for i in range(3264,3398):
    for j in range(0,96):
        outfile.write("100" + " " + str(j) + " " + str(counter*96+ 3264 +j) + "\n")
    counter+=1

outfile.write("\n")
outfile.close()



'''
###HAIMA

outfile = open("./trace" + ".txt", "w")

for i in range(0,32):
    for j in range(0,32):
        outfile.write(str(j)+ " " + str((j+1)%16) + " " + str(i) + "\n")


for i in range(32,64):
    for j in range(32,64):
        outfile.write(str(j)+ " " + str((j+1)%32) + " " + str(i) + "\n")

counter=0
for i in range(0,32):
    for j in range(32,96):
        outfile.write("100" + " " + str(j) + " " + str(counter*64+ 48+j) + "\n")
    counter+=1



outfile.write("\n")
outfile.close()
'''
