Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
Input format :
Integer N (Total no. of rows)
Constraints:
1 <= n <= 50
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
202
3003
40004


n=int(input())
print(1)
i=1
while(i<n):
    j=0
    while(j<i+1):
        if(j==0 or j==i):
            print(i,end="")
        else:
            print(0,end="")
        j=j+1
    i=i+1
    print()
