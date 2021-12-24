class Array:

    def __init__(self):
        self.capacity = 2
        self.baseArray = [None] * self.capacity
        self.count = 0

    def __len__(self):
        i = 0
        for el in self.baseArray:
            i += 1
        return i

    def __str__(self):
        output = ""
        for i in range(self.count):
            output += str(self.baseArray[i]) + ","

        return output[:-1]

    def _increaseCapacity(self, newCapacity):
        if newCapacity < self.capacity:
            raise ValueError("Новый capacity не может быть ниже настоящего")

        newAr = [None] * newCapacity

        i = 0
        for el in self.baseArray:
            newAr[i] = el
            i += 1

        self.capacity = newCapacity
        self.baseArray = newAr

    def get(self, order):
        return self.baseArray[order]

    def add(self, value):
        if self.count >= self.capacity:
            self._increaseCapacity(self.capacity * 2)

        self.baseArray[self.count] = value
        self.count += 1

    def set(self, order, value):
        self.baseArray[order] = value

    def orderOf(self, value):
        i = 0
        for el in self.baseArray:
            if el == value:
                return i
            i += 1

        return -1

    def remove(self, value):
        order = self.orderOf(value)
        if order == -1:
            raise ValueError("Value not found")

        self.removeAt(order)

    def removeAt(self, order):
        if order < 0 or order >= self.count:
            raise IndexError("Некорректный номер элемента")

        self.count -= 1
        for i in range(order, self.count):
            self.baseArray[i] = self.baseArray[i + 1]

        self.baseArray[self.count] = None

    def isEmpty(self):
        return self.count == 0