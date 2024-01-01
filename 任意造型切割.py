import rhinoscriptsyntax as rs
import rhinoscript as ge
Curve = None
pts = []
any = None
rs.AddNurbsSurface(points=any,point_count=any)

for i in range(10):
    for j in range(10):
        point=rs.AddPoint
        pts.append(point)
b = rs.PointCoordinates(Curve,point)
