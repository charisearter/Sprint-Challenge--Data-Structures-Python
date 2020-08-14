class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # max size it can be
        self.data = []  # holds the data

    def append(self, item):
        self.data.append(item)  # add item to end
        if len(self.data) == self.capacity:  # if at max capacity
            self.data.pop(0)  # remove at index 0
            self.data.append(item)  # add item to end

    def get(self):
        return self.data  # return the list of elements of not full
