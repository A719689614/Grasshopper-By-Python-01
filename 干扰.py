import rhinoscriptsyntax as rs
import random as r
pts = []
y = 0
while y < sample:
    for x in range(num):
        pts.append(rs.AddPoint(y*size, x*size))
        print(pts)
    y += 1
a = pts
# 创建一个空列表
list = []
attractor = rs.AddPoint(r.random()*scale, r.random()*scale, 0)
b = attractor
for i in range(len(pts)):
    distance = rs.Distance(pts[i], b)
    list.append(distance)
circlelist = []
c = circlelist
for i in range(len(pts)):
    radius = (list[i]/max(list)*size/2)
    circle = rs.AddCircle(pts[i],radius)
    circlelist.append(circle)
d = circlelist