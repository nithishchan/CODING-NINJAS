You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
 Output format :
For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
 Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
9 2 3 3 2 9 -1
Sample Output 1 :
true
Sample Input 2 :
2
0 2 3 2 5 -1
-1
Sample Output 2 :
false
true





from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)
#Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printll(head):
    list = []
    while head is not None:
        list.append(head.data)
        head=head.next
        return list
def reverseLL(head):
    list = []
    while head is not None:
        list.insert(0,head.data)
        head=head.next
        return list
def isPalindrome(head):
    if printll(head) == reverseLL(head):
        return True
    else:
        return False
def takeInput():
    head = None
    tail = None
    datas = list(map(int, stdin.readline().rstrip().split(" ")))
    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        i += 1
    return head
#to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.date,end="")
        head=head.next
    print()
#main
t = int(stdin.readline().rstrip())
while t > 0:
    head = takeInput()
    if isPalindrome(head):
        print('true')
    else:
        print('false')
    t -= 1
