from list import List
from queue import Queue
from stack import Stack
from algorithm import Graph
from arr import Array


class Traversal:

    @staticmethod
    def BreadthFirstSearch(graph: Graph):
        usedNodes = Array()
        resultArray = Array()

        q = Queue()
        first = graph.vertexList.get(0)
        q.enqueue(first)
        usedNodes.add(first)

        while not q.isEmpty():
            cur = q.dequeue()

            resultArray.add(cur)

            for edge in graph.edgesList.baseArray:
                if edge is not None:
                    fr = edge.fromNode
                    to = edge.toNode

                    if cur == fr and usedNodes.orderOf(to) == -1:
                        q.enqueue(to)
                        usedNodes.add(to)
                    elif cur == to and usedNodes.orderOf(fr) == -1:
                        q.enqueue(fr)
                        usedNodes.add(fr)

        return resultArray

    @staticmethod
    def DepthFirstSearch(graph: Graph):
        usedNodes = Array()
        resultArray = Array()

        st = Stack()
        st.push(graph.vertexList.get(0))

        while not st.isEmpty():
            cur = st.pop()

            if usedNodes.orderOf(cur) == -1:
                usedNodes.add(cur)
                resultArray.add(cur)

            for edge in graph.edgesList.baseArray:
                if edge is not None:
                    fr = edge.fromNode
                    to = edge.toNode

                    if cur == fr and usedNodes.orderOf(to) == -1:
                        st.push(to)
                    elif cur == to and usedNodes.orderOf(fr) == -1:
                        st.push(fr)

        return resultArray
