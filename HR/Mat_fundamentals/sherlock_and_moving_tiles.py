#https://www.hackerrank.com/challenges/sherlock-and-moving-tiles?h_r=next-challenge&h_v=zen
#http://stackoverflow.com/questions/38094109/hackerrank-time-taken-for-two-squares-to-overlap



import sys
import math
inputs =[]
for line in sys.stdin:
    inputs.append(line)

line = inputs[0].split(' ')
length = int(line[0])
speed1 = int (line[1])
speed2 = int (line[2])

for area in inputs[2:]:
    speed = abs(speed2 - speed1)
    temp = math.sqrt(2) *(length - math.sqrt(int(area)))
    t = temp/float(speed)
    print "{:.7f}".format(t)