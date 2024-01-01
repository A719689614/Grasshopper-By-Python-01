import rhinoscriptsyntax as rs
import random
import math as m
pts = []
attractor = rs.AddPoint(random.randint(-10, 100), random.randint(-10, 100), 0)

for x in range(10):
    for y in range(10):
        pts.append(rs.AddPoint(y*size, x*size))

a = pts
distance_list = []

for i in range(len(pts)):
    distance = rs.Distance(pts[i], attractor)
    distance_list.append(distance)

circlelist = []
for i in range(len(pts)):
    radius = abs(m.sin(m.radians(distance_list[i])*f)*size/2)
    circle = rs.AddCircle(pts[i], radius)
    circlelist.append(circle)
b = circlelist
