import rhinoscriptsyntax as rs
import random
pts = []

for i in range(100):
    pt = rs.AddPoint(random.randint(1,100),random.randint(1,100),0)
    pts.append(pt)
a = pts
curve = rs.AddPolyline(pts)
b = curve


