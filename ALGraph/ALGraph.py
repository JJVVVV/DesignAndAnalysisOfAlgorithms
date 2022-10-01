"""
-*- coding: utf-8 -*-
@Time    : 2022/10/1 10:43
@Author  : JIE
@Email   : wang-junjie@qq.com
@File    : DesignAndAnalysisOfAlgorithms-> ALGraph.py
@Software: PyCharm
"""
from .ArcNode import ArcNode
from .VNode import VNode


class ALGraph:
    def __init__(self, vexnum, arcnum=None, filepath=None):
        self.vexnum = vexnum
        self.arcnum = arcnum
        self.filepath = filepath
        self.vertexes: list[VNode] = [VNode() for _ in range(vexnum)]

    def create(self):
        if self.filepath:
            with open(self.filepath, 'r', encoding='utf8') as f:
                lines = f.readlines()
                self.arcnum = len(lines)
                for line in lines:
                    srcVexIdx, destVexIdx = list(map(lambda x: int(x) - 1, line.split()))
                    arcnode = ArcNode(destVexIdx, self.vertexes[srcVexIdx].first)
                    self.vertexes[srcVexIdx].first = arcnode
        else:
            pass

    def createReverseGraph(self):
        G_T: ALGraph = ALGraph(self.vexnum, self.arcnum)
        for srcVexIdx in range(self.vexnum):
            G_T.vertexes[srcVexIdx].data = self.vertexes[srcVexIdx].data
            arcPtr = self.vertexes[srcVexIdx].first
            while arcPtr:
                destVexIdx = arcPtr.adjVexIdx
                arcnode = ArcNode(srcVexIdx, G_T.vertexes[destVexIdx].first, arcPtr.weight)
                G_T.vertexes[destVexIdx].first = arcnode
                arcPtr = arcPtr.next
        return G_T

    def topoSort(self) -> tuple[list, list]:
        curLable = self.vexnum
        # f = [0] * self.vexnum
        stk = []
        visited = [False] * self.vexnum

        def dfs(srcVexIdx):
            nonlocal self, curLable, visited
            visited[srcVexIdx] = True
            arcptr = self.vertexes[srcVexIdx].first
            while arcptr:
                destVexIdx = arcptr.adjVexIdx
                if not visited[destVexIdx]:
                    dfs(destVexIdx)
                arcptr = arcptr.next
            # f[srcVexIdx] = curLable
            stk.append(srcVexIdx)
            curLable -= 1

        for srcVexIdx in range(self.vexnum):
            if not visited[srcVexIdx]:
                dfs(srcVexIdx)
        # return f, stk
        return stk

    def kasaraju(self):
        G_T = self.createReverseGraph()
        # f, stk = G_T.topoSort()
        stk = G_T.topoSort()
        visited = [False] * self.vexnum
        numSCC = 0
        scc = [0] * self.vexnum

        def dfs(srcVexIdx):
            nonlocal self, visited, scc
            visited[srcVexIdx] = True
            scc[srcVexIdx] = numSCC
            arcptr = self.vertexes[srcVexIdx].first
            while arcptr:
                destVexIdx = arcptr.adjVexIdx
                if not visited[destVexIdx]:
                    dfs(destVexIdx)
                arcptr = arcptr.next

        while stk:
            srcVexIdx = stk.pop()
            if not visited[srcVexIdx]:
                numSCC += 1
                dfs(srcVexIdx)

        return scc
