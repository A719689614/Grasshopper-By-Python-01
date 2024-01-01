import rhinoscriptsyntax as rs
pts = []
curvelist = []
for i in range(10):
    for j in range(10):
        pts.append(rs.AddPoint(i*size, j*size))
a = pts
# 矩阵点完成

for k in range(len(pts)):
    interpoly = []
    for l in range(degree):
        tmpvec = rs.VectorCreate(att, pts[k])
        unitvec = rs.VectorUnitize(tmpvec)
        vector = rs.VectorScale(unitvec, scale)
        vector = rs.VectorRotate(vector, degree, [0, 0, 1])
        newpt = rs.CopyObject(pts[k], vector)
        interpoly.append(newpt)
        pts[k] = newpt
    curve = rs.AddInterpCurve(interpoly)
    curvelist.append(curve)
b = curvelist
