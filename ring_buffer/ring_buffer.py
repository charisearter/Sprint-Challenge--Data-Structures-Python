class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # max size it can be
        self.data = []  # holds the data
        self.cur = 0

    def append(self, item):

        self.data.append(item)  # add item
        if len(self.data) == self.capacity:  # if at max capacity
            self.data.pop(0)
            self.data[self.cur] = item  # replace with item
            # next will replace next index of list

            self.cur = (self.cur+1) % self.capacity

    def get(self):
        return self.data  # return the list of elements of not full
