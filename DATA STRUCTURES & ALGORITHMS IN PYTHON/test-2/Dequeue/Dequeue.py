You need to implement a class for Dequeue i.e. for double ended queue. In this queue, elements can be inserted and deleted from both the ends.
You don't need to double the capacity.
You need to implement the following functions -
1. constructor
You need to create the appropriate constructor. Size for the queue passed is 10.
2. insertFront -
This function takes an element as input and insert the element at the front of queue. Insert the element only if queue is not full. And if queue is full, print -1 and return.
3. insertRear -
This function takes an element as input and insert the element at the end of queue. Insert the element only if queue is not full. And if queue is full, print -1 and return.
4. deleteFront -
This function removes an element from the front of queue. Print -1 if queue is empty.
5. deleteRear -
This function removes an element from the end of queue. Print -1 if queue is empty.
6. getFront -
Returns the element which is at front of the queue. Return -1 if queue is empty.
7. getRear -
Returns the element which is at end of the queue. Return -1 if queue is empty.
Input Format:
For C++ and Java, input is already managed for you. You just have to implement given functions.

For Python:
The choice codes and corresponding input for each choice are given in a new line. The input is terminated by integer -1. The following table elaborately describes the function, their choice codes and their corresponding input - 
Alt Text

Output Format:
For C++ and Java, output is already managed for you. You just have to implement given functions.

For Python: 
The output format for each function has been mentioned in the problem description itself. 
Sample Input 1:
5 1 49 1 64 2 99 5 6 -1
Sample Output 1:
-1
64
99





import collections
inp_ls = list(map(int, input().split()))
itr = 0
queue = collections.deque()
n = 0
while inp_ls[itr] != -1:
    choice = inp_ls[itr]
    if(choice == 1):
        itr = itr+1
        if(n <= 9):
            queue.appendleft(inp_ls[itr])
            n += 1
        else:
            print(-1)
    elif(choice == 2):
        itr = itr+1
        if(n <= 9):
            queue.append(inp_ls[itr])
            n += 1
        else:
            print(-1)
    elif(choice == 3):
        if(n >= 1):
            queue.popleft()
            n -= 1
        else:
            print(-1)
    elif(choice == 4):
        if(n >= 1):
            queue.pop()
            n -= 1
        else:
            print(-1)
    elif(choice == 5):
        if(n >= 1):
            element = queue.popleft()
            print(element)
            queue.appendleft(element)
        else:
            print(-1)
    elif(choice == 6):
        if(n >= 1):
            element = queue.pop()
            print(element)
            queue.append(element)
        else:
            print(-1)
    itr = itr + 1
