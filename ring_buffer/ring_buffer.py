# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity  # max size it can be
#         self.data = []  # holds the data
#         self.cur = 0  # index of list

#     def append(self, item):
#         self.data.append(item)  # add item
#         if len(self.data) == self.capacity:  # if at max capacity
#             self.data[self.cur] = item  # replace with item
#             # next will replace next index of list
#             self.cur = (self.cur+1) % self.capacity

#     def get(self):
#         return self.data  # return the list of elements of not full
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # max size it can be
        self.data = []  # holds the data
        self.cur = 0

    def append(self, item):
        if len(self.data) == self.capacity:  # if at max capacity
            # replace node at index starting with 0 until end (self.cur is current index)
            self.data[self.cur] = item
            if self.cur + 1 == self.capacity:
                self.cur = 0
            else:
                self.cur += 1
        else:
            self.data.append(item)  # add item to end

    def get(self):
        return self.data  # return the list of elements of not full
