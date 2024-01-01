import rhinoscriptsyntax as rs

dividepts = []
tmp =[]
domain = rs.CurveDomain(crv)
start = domain[0]
end = domain[1]
step = (end - start)/n

for x in range(start,end,step):
    point = rs.EvaluateCurve(crv,x)
    dividepts.append(point)
    tmp.append(x)

a = dividepts
b = tmp
