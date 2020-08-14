class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # max size it can be
        self.data = []  # holds the data

    class __Full:  # if Full
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.capacity

        def get(self):
            # ask TL about this syntax (What is it?)
            # return elements in list in correct order
            return self.data[self.cur:] + self.data[:self.cur]

    def append(self, item):
        self.data.append(item)  # add item
        if len(self.data) == self.capacity:  # if at max capacity
            self.cur = 0  # current
            # change class to full
            self.__class__ = self.__Full

    def get(self):
        return self.data  # return the list of elements of not full
