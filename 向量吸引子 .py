import rhinoscriptsyntax as rs
import random as r
# pts = []
# pt = rs.AddPoint(0, 0, 0)
# pts.append(pt)
pts = []



def function(pt1, pt2, scale):
    tmp = rs.VectorCreate(pt2, pt1)       # 创建向量
    univector = rs.VectorUnitize(tmp)        # 使向量成为单位向量
    vector = rs.VectorScale(univector, scale)  # 缩/放向量
    tempt = rs.CopyObject(pt1, vector)  # 用点1 沿着缩放向量进行复制
    line = rs.AddLine(pt1, tempt)      # 点1和之前的点连接
    return tempt, line                 # 返回值-> 点 和连接的线

new_pt= []
line_list = []
for i in range(10):
    for j in range(10):
        pt = rs.AddPoint(i, j, 0)
        pts.append(pt)

for i in range(len(pts)):
    pt, line = function(pts[i], attractor,scale)
    new_pt.append(pt)
    line_list.append(line)
a = new_pt
b = line_list


