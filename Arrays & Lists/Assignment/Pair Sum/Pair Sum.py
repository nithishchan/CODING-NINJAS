You have been given an integer array/list(ARR) and a number X. Find and return the total number of pairs in the array/list which sum to X.
Note:
Given array/list can contain duplicate elements. 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
Output format :
For each test case, print the total number of pairs present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= X <= 10^9
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



def duplicate (list1,sum):
    sum_time=0
    size=len(list1)
    for i in range(0,size):
        for j in range(i+1,size):
            if list1[i] + list1[j]==sum:
                sum_time+=1
            else:
                continue
    print(sum_time)

n=int(input()) #First Input
for i in range(n):
    faltu1=int(input()) #Secound input #no of ele in list
    if faltu1!=0:
        list = [int(x) for x in input().split()]
    X=int(input()) #3rd Input
    if faltu1!=0 :
        duplicate(list,X)
    else:
        print(0)
