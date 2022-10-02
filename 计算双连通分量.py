"""
-*- coding: utf-8 -*-
@Time    : 2022/10/1 21:35
@Author  : JIE
@Email   : wang-junjie@qq.com
@File    : DesignAndAnalysisOfAlgorithms-> 计算双连通分量.py
@Software: PyCharm
"""
from ALGraph import ALGraph

if __name__ == '__main__':
    filepath = ['./data/test1.txt', './data/test2.txt']
    vexnum = [16, 12]
    for i in range(len(filepath)):
        G = ALGraph(vexnum[i], filepath=filepath[i])
        G.create()
        for i in range(G.vexnum):
            G.vertexes[i].data = chr(ord('a') + i)
        ret = G.biconnectedComponent(0)
        print(len(ret))
        for component in ret:
            print(list(map(lambda item: G.vertexes[item[0]].data + G.vertexes[item[1]].data, component)))
