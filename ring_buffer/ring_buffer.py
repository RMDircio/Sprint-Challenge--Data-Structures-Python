class RingBuffer:
    def __init__(self, capacity):
        # capacity should be max_capacity
        self.capacity = capacity
        self.list = []
        self.next_index = 0 

    def append(self, item):
        ''' attach item on RingBuffer class '''
        # insert the item into the list at the next index
        self.list.insert(self.next_index, item)
        # create the next index
        # increase index by 1 and if remainder is 0, then index becomes 0
        self.next_index = (self.next_index + 1) % self.capacity

    def get(self):
        ''' print out all items (capacity) from RingBuffer class '''
        return self.list



# # manual tests
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']