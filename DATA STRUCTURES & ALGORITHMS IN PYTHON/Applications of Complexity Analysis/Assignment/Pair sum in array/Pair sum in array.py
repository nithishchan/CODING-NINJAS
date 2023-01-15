you have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
Note:
Given array/list can contain duplicate elements. 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'num'.
Output format :
For each test case, print the total number of pairs present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^4
0 <= num <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7
Sample Input 2:
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10
Sample Output 2:
0
2



from sys import stdin
from collections import OrderedDict

def pairSum(arr, n, num) :
    
    map = OrderedDict()
    ans = []
    
    for ele in arr:
        count = map.get(num - ele, 0)
        pair = [-1 for i in range(2)]
        pair[0] = ele
        pair[1] = num - ele

        while count > 0:
            ans.append(pair)
            count -= 1

        map[ele] = map.get(ele, 0) + 1

    res = [[-1 for j in range(2)] for i in range(len(ans))]

    for i in range(len(ans)):
        a = ans[i][0]
        b = ans[i][1]
        res[i][0] = min(a, b)
        res[i][1] = max(a, b)

    return len(res)

#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()

#main
t = int(stdin.readline().strip())

while t > 0 : 
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))
    t -= 1
