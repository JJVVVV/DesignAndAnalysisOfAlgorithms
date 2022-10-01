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
    filepath = ['./data/test1.txt']
    vexnum = [16]
    for i in range(len(filepath)):
        G = ALGraph(vexnum[i], filepath=filepath[i])
        G.create()
        ret = G.biconnectedComponent(0)
        print(ret)