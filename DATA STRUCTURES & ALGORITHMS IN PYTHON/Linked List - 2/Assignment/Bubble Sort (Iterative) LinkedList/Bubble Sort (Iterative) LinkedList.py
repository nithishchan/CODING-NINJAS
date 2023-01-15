Given a singly linked list of integers, sort it using 'Bubble Sort.'
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the sorted singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
0 <= M <= 10^3
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
10 9 8 7 6 5 4 3 -1
Sample Output 1 :
 3 4 5 6 7 8 9 10 
 Sample Input 2 :
10 -5 9 90 5 67 1 89 -1
Sample Output 2 :
-5 1 5 9 10 67 89 90 




from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubbleSortLL(head) :
   
    end = None
    while end != head:
        p = head
        while p.next != end:
            q = p.next
            if p.data > q.data:
                p.data, q.data = q.data, p.data
            p = p.next
        end = p

    return end           
        
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
        
    return head
    
def printll(head):
    while head:
        print(head.data, end = " ")
        head = head.next
    print()
    
arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = bubbleSortLL(l)
printll(l)
