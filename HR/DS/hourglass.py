#https://www.hackerrank.com/challenges/2d-array?h_r=next-challenge&h_v=zen

import sys
fl_name =  sys.argv[1]
fp = open(fl_name,'r')
lines  =  fp.readlines()

arr_temp=[]
for line in lines:
    arr_temp.append(map(int, line.strip().split( ' ')))

print arr_temp

for index,line in enumerate(arr_temp):
    print line[0:3], line[index+1][index+1]
                    # +line[index+2:3]
# for arr_i in xrange(6):
#     print raw_input()
#     # arr_temp = map(int,raw_input().strip().split(' '))
#     # arr.append(arr_temp)
#
# print arr