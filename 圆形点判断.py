import rhinoscriptsyntax as rs
pts=[]
circle = rs.AddCircle([0,0,0],500)
x = 0
while x < 30:
    y = 0
    while y < 30:
        point = rs.AddPoint(x,y)
        pts.append(point)
        y += 1
    x += 1
newpts = []
a = pts
for i in range(len(pts)):
    b = rs.Distance(i,[0,0,0])
    if b < 500:
        newpts.append(i)

c =newpts
any = None
for j in range(len(c)):
    dis = rs.Distance(c[j],[0,0,0])
    distance = (dis/500)
    rec = rs.AddRectangle(c[j],width=any,height=any)
    rs.ScaleObject(rec,scale=distance,bool=False)
    