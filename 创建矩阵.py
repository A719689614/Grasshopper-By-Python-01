import rhinoscriptsyntax as rs
import random
pts = []
pt = rs.AddPoint(x, y, z)
a = pt
pts.append(pt)
for i in range(randomint):
    vector = (random.randint(1,500), random.randint(-100, 500), 0)
    tmp = rs.CopyObject(pts[-1], vector)
    pts.append(tmp)
    curve = rs.AddCurve(pts)


b = pts
c = curve
d = vector
