"""
-*- coding: utf-8 -*-
@Time    : 2022/10/1 10:33
@Author  : JIE
@Email   : wang-junjie@qq.com
@File    : DesignAndAnalysisOfAlgorithms-> 计算强连通分量.py
@Software: PyCharm
"""
import heapq
import sys
from collections import Counter

from ALGraph import ALGraph

sys.setrecursionlimit(100000)  # 例如这里设置为一百万
if __name__ == '__main__':
    filepath = ['./data/problem8.10test1.txt', './data/problem8.10test2.txt',
                './data/problem8.10test3.txt', './data/problem8.10test4.txt',
                './data/problem8.10test5.txt', './data/problem8.10.txt']
    vexnum = [9, 8, 8, 8, 12, 875714]
    for i in range(5):
        G = ALGraph(vexnum[i], filepath=filepath[i])
        G.create()
        scc = G.kasaraju()
        cnt = Counter(scc)
        # print(scc)
        top5 = heapq.nlargest(5, cnt.values())
        top5.extend([0] * (5 - len(top5)))
        print(f'Top 5 scc size: {top5}')
