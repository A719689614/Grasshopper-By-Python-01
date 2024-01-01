import rhinoscriptsyntax as rs
import random as r


def vector(pt1, pt2, scale):
    tmpvec = rs.VectorCreate(pt1, pt2)
    unitvec = rs.VectorUnitize(tmpvec)
    vec = rs.VectorScale(unitvec, scale)
    newpt = rs.CopyObject(pt1, vec)
    line = rs.AddLine(pt1, newpt)

    return newpt, line


pts = []
newpt = []
linelist = []
for i in range(10):
    for j in range(10):
        pt = rs.AddPoint(i, j, 0)
        pts.append(pt)
a = pts

for i in range(len(pts)):
    pt, line = vector(pts[i], attractor, scale)
    newpt.append(pt)
    linelist.append(line)

a = pts
b = newpt
c = linelist

