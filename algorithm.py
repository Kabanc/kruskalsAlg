from sort import bubbleSort
from arr import Array
from disjointset import Edge
from disjointset import DisjointSet


class Graph:
    def __init__(self):
        self.edgesList = Array()
        self.vertexList = Array()

    def addEdge(self, vertex1: str, vertex2: str, weight: int):
        self.edgesList.add(Edge(vertex1, vertex2, weight))
        self.vertexList.add(vertex1)
        self.vertexList.add(vertex2)

    def __str__(self):
        ans = ""
        for i in self.edgesList.baseArray:
            ans += str(i) + "\n"
        return ans

    def kruskal(self):
        result = Array()
        disjointSet = Array()

        for i in self.vertexList.baseArray:
            if i is not None:
                disjointSet.add(DisjointSet(i, None))

        bubbleSort.bubbleSortForEdges(self.edgesList)

        for i in self.edgesList.baseArray:
            if i is None:
                continue

            element = self.findInDsu(disjointSet, i.fromNode)
            element2 = self.findInDsu(disjointSet, i.toNode)

            repr1 = element.representative()
            repr2 = element2.representative()

            if repr1 == repr2:
                continue

            result.add(i)
            element.union(element2)

        return result

    def findInDsu(self, disjointSet, node):
        for i in disjointSet.baseArray:
            if i is not None:
                if i.node == node:
                    return i

        raise RuntimeError("vertex not found")

    def read_file(self):
        line = " "
        with open('edges.txt') as file:
            while line != '':
                line = file.readline()
                p = line.split(sep=" ")

                if len(p) == 3:
                    p1, p2, p3 = p[0], p[1], p[2]
                    self.addEdge(p1, p2, int(p3))

def testDSE():
    element1 = DisjointSet("A", None)
    element2 = DisjointSet("B", element1)
    element3 = DisjointSet("C", element2)
    element4 = DisjointSet("D", element2)

    assert element1.representative() == element1
    assert element2.representative() == element1
    assert element3.representative() == element1
    assert element4.representative() == element1

    # test 2
    element1 = DisjointSet("A", None)
    element2 = DisjointSet("B", element1)
    element3 = DisjointSet("C", None)
    element4 = DisjointSet("D", element3)

    element1.union(element4)

    assert element1.representative() == element3
    assert element2.representative() == element3
    assert element3.representative() == element3
    assert element4.representative() == element3
    print("success")


def testSort():
    a = Graph()
    a.addEdge('A', 'B', 10)
    a.addEdge('A', 'C', 5)
    a.addEdge('A', 'L', 4)
    a.addEdge('A', 'Q', 14)
    a.addEdge('A', 'E', 3)
    a.addEdge('B', 'C', 20)
    a.addEdge('B', 'C', 1)
    bubbleSort.bubbleSortForEdges(a.edgesList)
    print(a.edgesList)


if __name__ == '__main__':
    # test_DSE()
    # test_sort()
    a = Graph()
    a.addEdge("A", "B", 7)
    a.addEdge("A", "D", 5)
    a.addEdge("D", "B", 9)
    a.addEdge("D", "E", 15)
    a.addEdge("D", "F", 6)
    a.addEdge("B", "C", 8)
    a.addEdge("B", "E", 7)
    a.addEdge("F", "E", 8)
    a.addEdge("F", "G", 11)
    a.addEdge("G", "E", 9)
    a.addEdge("E", "C", 5)
    result = a.kruskal()

    sum = 0

    res = Array()
    for edge in result.baseArray:
        if edge is not None:
            res.add(str(edge))
            sum += edge.weight

    bubbleSort.bubbleSortLexicographic(res)

    for edgeText in res.baseArray:
        if edgeText is not None:
            print(edgeText)

    print(sum)