"""
-*- coding: utf-8 -*-
@Time    : 2022/10/1 21:35
@Author  : JIE
@Email   : wang-junjie@qq.com
@File    : DesignAndAnalysisOfAlgorithms-> 计算双连通分量.py
@Software: PyCharm
"""
import random
import sys

from ALGraph import ALGraph, ArcNode

sys.setrecursionlimit(10000)


def test():
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


def question(vexnum: int):
    def generateGraph(vexnum: int) -> ALGraph:
        G = ALGraph(vexnum)
        for srcVexIdx in range(vexnum):
            for _ in range(5):
                destVexIdx = srcVexIdx
                while destVexIdx == srcVexIdx:
                    destVexIdx = random.randint(0, vexnum - 1)
                arcnode = ArcNode(destVexIdx, G.vertexes[srcVexIdx].first)
                G.vertexes[srcVexIdx].first = arcnode
                arcnode = ArcNode(srcVexIdx, G.vertexes[destVexIdx].first)
                G.vertexes[destVexIdx].first = arcnode
        return G

    G = generateGraph(vexnum)
    ret = G.biconnectedComponent(0)
    print(len(ret))
    for component in ret:
        print(component)


if __name__ == '__main__':
    test()
    print()
    for _ in range(10):
        question(1000)
    print()
    for _ in range(10):
        question(10000)
