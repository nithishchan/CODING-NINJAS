Implement the class for Max Priority Queue which includes following functions -
1. getSize -
Return the size of priority queue i.e. number of elements present in the priority queue.
2. isEmpty -
Check if priority queue is empty or not. Return true or false accordingly.
3. insert -
Given an element, insert that element in the priority queue at the correct position.
4. getMax -
Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.
5. removeMax -
Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty.
Note : main function is given for your reference which we are using internally to test the class.

  
  class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def __percolateDown(self):
        parentIndex = 0
        leftIndex = 2*parentIndex + 1
        rightIndex = 2*parentIndex + 2
        while leftIndex < self.getSize():
            minIndex = parentIndex
            if(self.pq[minIndex].priority < self.pq[leftIndex].priority):
                minIndex = leftIndex
            if(rightIndex < self.getSize() and self.pq[minIndex].priority < self.pq[rightIndex].priority):
                minIndex = rightIndex
            
            if minIndex!=parentIndex:
                self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
                parentIndex = minIndex
                leftIndex = 2*parentIndex + 1
                rightIndex = 2*parentIndex + 2
            else:
                break
            
            
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def removeMax(self):
        if self.isEmpty():
            return None
        element = self.pq[0]
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return element.ele
        

myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
