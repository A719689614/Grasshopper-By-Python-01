import rhinoscriptsyntax as rs
import random as r

# vector = (3, 4, 5)

# a = rs.VectorLength(vector)

# b = rs.VectorScale(vector, scale=2.3)

# rs.VectorLength(b)

# vector_new = rs.VectorCreate(rs.AddPoint(
#     r.random(), r.random(), r.random()), (0, 5, r.random()))

# vector_A = rs.VectorRotate(vector, 90, vector_new)


# 向量的加减乘除
# vector_B = (4,0,0) # 向量的写法为圆括号
# vector_B = (2,5,0)
# rs.VectorSubtract(vector_A,vector_B)
# rs.VectorCrossProduct()

# 向量角度
# rs.VectorAngle(vector_A,vector_B)


# 范例
pts= []
pt = rs.AddPoint(0,0,0)
pts.append(pt)


vector = (1,0,0)

for i in range(5):
    Newpt = rs.CopyObject(pts[-1],vector)
    pts.append(Newpt)
    tmp = rs.CopyObject(pts[-1],vector)
    pts.append(tmp)
     
a = pts

