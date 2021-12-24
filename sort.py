from list import List
from listEl import El
from arr import Array

class bubbleSort:
    @staticmethod
    def bubbleSortForEdges(l: Array):
        if type(l) is not Array:
            raise TypeError("l is not array")

        n = len(l)
        for i in range(n):
            for j in range(0, n - i - 1):
                if l.baseArray[j] is not None and l.baseArray[j + 1] is not None:
                    if l.baseArray[j].weight > l.baseArray[j + 1].weight:
                        l.baseArray[j], l.baseArray[j + 1] = l.baseArray[j + 1], l.baseArray[j]

    @staticmethod
    def bubbleSortLexicographic(l: Array):
        n = len(l)
        for i in range(n):
            for j in range(0, n - i - 1):
                if l.baseArray[j] is not None and l.baseArray[j + 1] is not None and l.baseArray[j] > l.baseArray[j + 1]:
                    l.baseArray[j], l.baseArray[j + 1] = l.baseArray[j + 1], l.baseArray[j]





