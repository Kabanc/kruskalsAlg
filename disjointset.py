from arr import Array
from sort import bubbleSort


class DisjointSet:

    def __init__(self, node, parent):
        self.rank = 0
        self.parent = parent
        self.node = node

    def union(self, set2):
        repr = self.representative()
        repr2 = set2.representative()

        if repr.rank > repr2.rank:
            repr2.parent = repr
        elif repr.rank < repr2.rank:
            repr.parent = repr2
        else:
            repr.parent = repr2
            repr2.rank += 1

    def representative(self):
        el = self
        while el.parent is not None:
            el = el.parent

        return el


class Edge:
    def __init__(self, fromNode: str, toNode: str, weight: int):
        self.fromNode = fromNode
        self.toNode = toNode
        self.weight = weight

    def __str__(self):
        return self.fromNode + " " + self.toNode
