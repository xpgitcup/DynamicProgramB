import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# for i in range(3):
# G.add_node(i)
G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5), (0, 2, 5.5)])  # 添加边的权值
pos = [(1, 1), (1, 2), (2, 2)]  # 元组中的两个数字是第i（从0开始计数）个点的坐标
print(pos)
print(type(pos))
print(type(pos[0]))
nx.draw(G, pos, with_labels=True, node_color='b')  # 按参数构图
plt.xlim(0, 5)  # 设置首界面X轴坐标范围
plt.ylim(0, 5)  # 设置首界面Y轴坐标范围

plt.show()  # 显示图像
