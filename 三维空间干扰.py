import rhinoscriptsyntax as rs
import random as rm
pts = []

for i in range(n):
    for j in range(n):
        for k in range(n):
            pts.append(rs.AddPoint(i*size, j*size, k*size))

a = pts

attractor = rs.AddPoint(rm.randint(
    0, 30), rm.randint(0, 30), rm.randint(0, 30))
b = attractor
distance_list = []
for i in range(len(pts)):
    distance = rs.Distance(pts[i], attractor)
    distance_list.append(distance)
distance = distance_list

rectangle_list = []
for i in range(len(pts)):
    plane = rs.PlaneFromNormal(pts[i], normal=(
        rs.VectorCreate((0, 0, 0), (0, 0, 1))))
    rectangle = rs.AddRectangle(plane, f, f)
    rectangle_list.append(rectangle)
c = rectangle_list

new_list = []
for i in range(len(c)):
    new = rs.ScaleObject(c[i],pts[i],(distance[i]/sc,distance[i]/sc,distance[i]/sc))
    new_list.append(new)
fn = new_list
    

