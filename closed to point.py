import rhinoscriptsyntax as rs                 # 导入rhino语法

pts = []                                       # 设定空列表用来获取矩阵

for x in range(n):
    for y in range(n):
        pt = rs.AddPoint(x*size, y*size, z=0) # size不是报错哦！是在GH里设为变量，可以进行参数调整
        pts.append(pt)                         # 将点添加到列表待用（枚举）
a = pts       
distance_list = []                             # 设定空列表待用（添加距离数据）
for i in range(len(pts)):                      # 对刚刚的矩阵进行枚举获得相对应的位置点              
    t = rs.CurveClosestPoint(curve,pts[i],segment_index)     # 获取nurbs曲线上的t值（枚举点到线的距离）
    pt_oncurve = rs.EvaluateCurve(curve,t)                   # 获取所有在曲线上的点值
    distance = rs.Distance(pts[i],pt_oncurve)                # 枚举点到nurbs曲线点的距离
    distance_list.append(distance)                           # 添加到距离列表待用

circle_list = []                                             # 这里举例用circle ，可以用其他图形，不唯一
for i in range(len(pts)):                                    # 生成图形的位置当然还是枚举点的位置拉                       
    radius = (distance_list[i]/max(distance_list)*size/2)    # 半径的值不能大于各自枚举点距离的最大值的1/2
    circle = rs.AddCircle(pts[i],radius)                     # （这里数学不好的看不懂就跳过）接上一行注释，然后画圆
    circle_list.append(circle)                               # 生成的圆添加到集合列表

b = circle_list                                              # 从b通道输出
# 以上代码红线处，不是报错哦，这里的代码在python里是跑不了的，只能在GHpython里面跑