# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random

num_enqueue = 0
num_dequeue = 0
num_full = 0
num_empty = 0

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

# Write a random tester for the Queue class.
def test():
    for i in range(8000):
        randomly_test_queue()
        
    print_stats()


def randomly_test_queue():
    global num_enqueue, num_dequeue, num_full, num_empty
    
    q_size = random.randint(1, 6)
    q = Queue(q_size)
    tracker_q = []
    
    for i in range(10):
        rand_int = random.randint(-1000000000, 1000000000)
        
        if random.random() < 0.6:
            result = q.enqueue(rand_int)
            num_enqueue += 1
            q.checkRep()
            
            if len(tracker_q) == q_size:
                num_full += 1
                assert not result
            else:
                tracker_q.append(rand_int)
                assert result
        else:
            result = q.dequeue()
            num_dequeue += 1
            q.checkRep()
            
            if len(tracker_q) - 1 < 0:
                num_empty += 1
                assert result is None
            else:
                removed_val = tracker_q.pop(0)
                assert removed_val == result


def print_stats():
    print('Total operations: {}'.format(num_enqueue + num_dequeue))
    print('Enqueues: {}'.format(num_enqueue))
    print('Dequeues: {}'.format(num_dequeue))
    print('Times full: {}'.format(num_full))
    print('Times empty: {}'.format(num_empty))
    
    
test()

