import rhinoscriptsyntax as rs
pt1 = rs.AddPoint(x, y, z)
pt2 = rs.AddPoint(u, v, w)
line = rs.AddLine(pt1, pt2)
a = rs.CurveLength(line)
b = pt2
