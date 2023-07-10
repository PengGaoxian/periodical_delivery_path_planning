# import pandas as pd
# # 读取excel文件
# read_excel = pd.read_excel('dataset(37).xlsx', sheet_name='Sheet1')
# # 读取read_excel中的第2列到第3列
# location = read_excel.iloc[:, 1:3]
# lng = location.iloc[:, 0]
# lat = location.iloc[:, 1]
# # 以列表lng中的数据为横坐标，列表lat中的数据为纵坐标，画图显示坐标位置
# import matplotlib.pyplot as plt
# plt.scatter(lng, lat)
# plt.show()
import Routes
# pts = Routes.getCommuteRoute()
# print(pts)
# 
# output = open("C:/Users/Administrator/Desktop/path.txt", 'w')
# output.write('x,y\n')
# for pt in pts:
#     output.write(pt + '\n')
# output.close()

Routes.getCommuteRoutes()