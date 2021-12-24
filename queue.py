from list import List


class Queue:
    def __init__(self):
        self.base_list = List()

    def dequeue(self):
        if self.base_list.head is None:
            raise RuntimeError("В очереди нет элементов")

        firstEl = self.base_list.head

        self.base_list.head = firstEl.next

        return firstEl.value

    def enqueue(self, value):
        self.base_list.add(value)

    def isEmpty(self):
        return self.base_list.head is None