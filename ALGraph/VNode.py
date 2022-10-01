"""
-*- coding: utf-8 -*-
@Time    : 2022/10/1 10:43
@Author  : JIE
@Email   : wang-junjie@qq.com
@File    : DesignAndAnalysisOfAlgorithms-> VNode.py
@Software: PyCharm
"""
from typing import Optional

from .ArcNode import ArcNode


class VNode:
    def __init__(self, data=None):
        self.data = data
        self.first: Optional[ArcNode] = None
