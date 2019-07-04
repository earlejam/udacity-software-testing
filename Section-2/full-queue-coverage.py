# TASK:
#
# Achieve full statement coverage on the Queue class. 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True
 
    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Add test code to test() that achieves 100% coverage of the 
# Queue class.
def test():

    q = Queue(3)
    assert q.empty()
    assert not q.full()
    
    no_item = q.dequeue()
    assert no_item is None
    
    q.enqueue(4)
    assert not q.empty()
    assert not q.full()
    
    q.enqueue(7)
    
    enough_room_left = q.enqueue(9)
    assert enough_room_left
    assert q.full()
    assert not q.empty()
    q.checkRep()
    
    enough_room_left = q.enqueue(11)
    assert not enough_room_left
    q.checkRep()
    
    first_item = q.dequeue()
    assert first_item == 4
    q.checkRep()
    
    q.dequeue()
    third_item = q.dequeue()
    assert third_item == 9
    assert q.empty()

test()

