import rhinoscriptsyntax as rs

pts = []

for x in range(n):
    for y in range(n):
        pts.append(rs.AddPoint(x*size, y*size, z=0))

pt_oncurve_list = []
distancelist = []
circle_list = []

t = []
for i in range(len(pts)):
    for j in curves:
        t = rs.CurveClosestPoint(j, pts[i])
        pt_oncurve= rs.EvaluateCurve(j,t)
        pt_oncurve_list.append(pt_oncurve)
    mindist = -1
    for k in range(len(pt_oncurve_list)):
        distance = rs.Distance(pts[i],pt_oncurve_list[k])
        if mindist <0 or distance <mindist:
            mindist = distance
    distancelist.append(distance)

for i in range(len(pts)):
    radius = (distancelist(i)/max(distancelist)*size/2)
    cricle = rs.AddCircle(pts[i],radius)
    circle_list.append(cricle)

a = circle_list
               
               