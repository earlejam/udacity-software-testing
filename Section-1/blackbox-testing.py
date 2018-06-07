# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    
    test_typical_usage_empty_and_full()
    test_for_integer_overflow()
    test_large_queue()
    
    
def test_typical_usage_empty_and_full():
    
    q = Queue(2)
    assert q.empty()
    assert not q.full()
    no_item_to_dq = q.dequeue()
    assert no_item_to_dq is None
    
    enqueue_succeeded = q.enqueue(1)
    assert enqueue_succeeded
    assert not q.empty()
    assert not q.full()
    
    enqueue_succeeded = q.enqueue(2)
    assert enqueue_succeeded
    assert not q.empty()
    assert q.full()
    
    room_for_another = q.enqueue(3)
    assert not room_for_another
    assert q.full()
    assert not q.empty()
    
    dq_a_1 = q.dequeue()
    assert dq_a_1 == 1
    assert not q.full()
    assert not q.empty()
    
    dq_a_2 = q.dequeue()
    assert dq_a_2 == 2
    assert not q.full()
    assert q.empty()
    
    nothing_dequeued = q.dequeue()
    assert nothing_dequeued is None
    assert q.empty()
    assert not q.full()
    
def test_for_integer_overflow():
    
    q = Queue(2)
    LARGE_INTEGER = 2**20
    enq_succeeded = q.enqueue(LARGE_INTEGER)
    assert enq_succeeded
    dq_large_integer = q.dequeue()
    assert dq_large_integer == LARGE_INTEGER
    
    
def test_large_queue():
    
    large_q = Queue(2**10)
    elems = [i for i in range(2**10)]

    for i in elems:
        succeeded = large_q.enqueue(i)
        assert succeeded
        
    for i in elems:
        dq_elem = large_q.dequeue()
        assert dq_elem == i

