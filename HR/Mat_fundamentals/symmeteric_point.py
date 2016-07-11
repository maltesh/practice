import sys
inputs =[]
for line in sys.stdin:
    inputs.append(line)

for points in inputs[1:]:
    pnts = points.split(" ")
    p = map( int, pnts[0:2])
    q = map(int ,pnts[2:])
    print 2*q[0]-p[0] ,2*q[1]-p[1]


#Notes
# Calculate the symmetric point of A = (7, 4) with the midpoint M = (3, −11).
# Point symmetry
# First it is necessary to define reflection of a point P through a point Q. The reflection of a point P across a point Q is the point P' such that Q is the midpoint of PP'. Points P and P' are said to be symmetric about Q.
#
# A geometric figure is said to have point symmetry if there is a point Q for which the reflection of every point P of the figure through Q is also a point of the figure.