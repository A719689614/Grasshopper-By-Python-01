import rhinoscriptsyntax as rs

domain = rs.CurveDomain(crv)
str = domain[0]
end = domain[1]

startpoint = rs.EvaluateCurve(crv,str)
endpoint = rs.EvaluateCurve(crv,end)

a = startpoint
b = endpoint