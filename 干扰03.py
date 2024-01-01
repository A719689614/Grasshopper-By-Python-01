import rhinoscriptsyntax as rs
import random as rm
pts = []

for i in range(20):
    for j in range(20):
        pts.append(rs.AddPoint(i*10, j*10, 0))

distancelist = []
attractor = rs.AddPoint(rm.randint(0, 20), rm.randint(0, 20), 0)

count = 0
while count < len(pts):
    distance = rs.Distance(attractor, pts[count])
    distancelist.append(distance)
    count += 1

rectlist = []

for i in range(len(pts)):
    plane = rs.PlaneFromNormal(pts[i], rs.VectorCreate([0, 0, 1], [0, 0, 0]))
    rect = rs.AddRectangle(plane, 5, 5)
    recr = rs.RotateObject(rect, pts[i], distancelist[i]*4)
    rectlist.append(rect)

a = rectlist
b = distancelist
c = pts
