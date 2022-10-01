"""
-*- coding: utf-8 -*-
@Time    : 2022/10/1 10:44
@Author  : JIE
@Email   : wang-junjie@qq.com
@File    : DesignAndAnalysisOfAlgorithms-> ArcNode.py
@Software: PyCharm
"""
from typing import Optional


class ArcNode:
    def __init__(self, destVexIdx, next=None, weight=None):
        self.adjVexIdx = destVexIdx
        self.weight = weight
        self.next: Optional[ArcNode] = next
