You will be given ‘Q’ queries. You need to implement a queue using two stacks according to those queries. Each query will belong to one of these three types:
1 ‘X’: Enqueue element ‘X’  into the end of the nth queue. Returns true after the element is enqueued.

2: Dequeue the element at the front of the nth queue. Returns -1 if the queue is empty, otherwise, returns the dequeued element.
Note:
Enqueue means adding an element to the end of the queue, while Dequeue means removing the element from the front of the queue.
Input Format:
The first line of input contains an integer ‘Q’ denoting the number of queries. 

The next ‘Q’ lines specify the type of operation/query to be performed on the data structure.

Each query contains an integer ‘P’ denoting the type of query.

For query of type 1, the integer ‘P’ is equal to 1 and it is followed by one integer ‘X’ denoting the element on which operation is to be performed.

For query of type 2, the integer ‘P’ is equal to 2 which dequeues the element.
Output Format:
For each query, return the output returned after performing the corresponding operation on the data structure. 
Note:
You don’t need to print anything. It has already been taken care of. Just implement the given functions.
Constraints:
1 <= Q <= 10^5 
1 <= P <= 2
1 <= X <= 10^5

Time limit: 1 sec
Sample Input 1:
7
1 2 
1 3 
2 
1 4 
1 6 
1 7 
2
Sample Output 1:
True 
True
2
True
True
True
3
from os import *
from sys import *
from collections import *
from math import *

    
class Queue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, data):
        #(O(n))
        while(len(self.__s1) != 0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)

        while(len(self.__s2) != 0):
            self.__s1.append(self.__s2.pop())
        return True

    def dequeue(self):
        #O(1)
        if len(self.__s1) == 0:
            return -1
        return self.__s1.pop()

    def front(self):
        if len(self.__s1) == 0:
            return -1
        return self.__s1[-1]

    def size(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.size() == 0


q = Queue()
#q.enqueue(1)
#q.enqueue(2)
#q.enqueue(3)
#q.enqueue(4)

while(q.isEmpty() is False):
    print(q.front())
    q.dequeue()
