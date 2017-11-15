#!/usr/bin/python
# Queue.py

""" Queue Class
Implement a growable and shrinkable queue with an array as
the underlying data structure
"""

import string

class Queue:

    def __init__(self, initial_capacity):
        """init: queue * num -> .
        purpose: initialize queue
        consumes: a queue and a number
        Produces: nothing
        Raises: InvalidInputException:  initial_capacity negative or null
        Example: Queue(9) -> An Empty Queue with space for 9 elements
        """

        if initial_capacity == 0 or initial_capacity == None:
            raise InvalidInputException
        self._data = [None] * initial_capacity
        self._capacity = initial_capacity
        self._count = 0
        self._head = 0
        self._tail = 0

    def size(self):
        """size: queue -> num
        purpose: returns number of items currently in queue
        consumes: a queue
        Produces: the number of items in the queue
        Example: size() -> 9
        """
        return self._count

    def is_empty(self):
        """is_empty: queue -> bool
        purpose: tell whether the queue is empty or not
        consumes: a queue
        Produces: boolean
        Example: is_empty() -> false
        """
        return self._count == 0

    def enqueue(self,element):
        """enqueue: queue * any -> .
        purpose: add an arbitrary type to the end of the queue
        consumes: a queue and an arbitrary type
        Produces: nothing
        Example: enqueue("sarah") -> the string sarah is added to the end of the queue
        """

        # If queue is at full capacity, we move elements to new array
        if self._count == self._capacity:
            new_capacity = self._capacity * 2
            new_data = [None] * (new_capacity)
            place = 0 # Variable to keep track of place in the new array
            count = self._count # Variable to keep track of elements in the old array
            while not count == 0:
                if self._head == self._capacity: # Loop around if at the end
                    self._head = 0
                new_data[place] = self._data[self._head]
                self._head += 1
                place += 1
                count -= 1
            # We have to reset the head, tail, capacity, and array
            self._tail =  self._capacity
            self._head = 0
            self._capacity = new_capacity
            self._data = new_data
        # If queue is not at full capacity but we've reached the end,
        # we must reset the tail
        if self._tail == self._capacity:
            self._tail = 0
        # If queue is not at full capacity we just add the element at the tail
        self._data[self._tail] = element
        self._count += 1
        self._tail += 1

    def dequeue(self):
        """dequeue: queue -> any
        purpose: removes and returns first item in queue
        (throws EmptyQueueException if empty)
        consumes: a queue
        Produces: first element in the queue
        Raises: EmptyQueueException: trying to dequeue from empty queue
        Example: dequeue() -> "sarah"
        """

        # Check that the queue is not empty
        if self._count == 0:
            raise EmptyQueueException(self)
        element = self._data[self._head]
        self._count -= 1
        # If the head is the last element in the array, we set the head to the front of the array
        if self._head == self._capacity - 1:
            self._head = 0
        else:
            self._head += 1
        # If after removing the element, the array is now a quarter full or less,
        # we must now move to an array that half the size
        if self._count <= self._capacity/4 and self._capacity > 3:
            new_capacity = self._capacity//2
            new_data = [None] * (new_capacity)
            place = 0 # Variable to keep track of place in the new array
            count = self._count # Variable to keep track of elements in old array
            while not count == 0:
                if self._head == self._capacity: # Loop around if at the end
                    self._head = 0
                new_data[place] = self._data[self._head]
                self._head += 1
                place += 1
                count -= 1
            # We have to reset the head, tail, capacity, and array
            self._tail = self._count
            self._head = 0
            self._capacity = new_capacity
            self._data = new_data
        return element

    def front(self):
        """front: queue ->  any
        purpose: returns first item in queue without removing it (throws empty queue exception if empty)
        consumes: a queue
        Produces: the first item in the queue
        Raises: EmptyQueueException: trying to find element from empty queue
        Example: front() -> "sarah"
        """

        # Check that the queue is not empty
        if self._count == 0:
            raise EmptyQueueException(self)
        element = self._data[self._head]
        # Does not alter the queue (the head remains at the same index)
        return element

    def capacity(self):
        """capacity: queue -> num
        purpose: returns how many elements the queue can hold
        consumes: a queue
        Produces: number of elements the queue can hold
        Example: capacity() -> 16
        """
        return self._capacity


class EmptyQueueException(Exception):
    """EmptyQueueException: Exception -> stack trace
    purpose: produce stack trace when an error is encountered due to an empty queue
    consumes: an exception
    Produces: stack trace
    Example: raise EmptyQueueException
    """
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidInputException(Exception):
    """InvalidInputException: Exception -> stack trace
    purpose: produce stack trace when an error is encountered due to an invalid input
    consumes: an exception
    produces: stack trace
    Example: raise InvalidInputException
    """
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
