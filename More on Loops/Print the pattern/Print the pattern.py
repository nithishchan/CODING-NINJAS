Print the following pattern for the given number of rows.
Pattern for N = 5
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
4
Sample Output :
 1  2  3  4
 9 10 11 12
13 14 15 16
 5  6  7  8
  
  n = int(input()) 
startValue = 1
for i in range(1,n+1): 
    for j in range(startValue,startValue + n):
        print(j,end=" ")
    print()
    if(i==((n+1)//2)):
        if((n%2)!=0):
            startValue = n*(n-2)+1
        else:
            startValue = n*(n-1) + 1
    elif((i>(n+1)//2)):
        startValue = startValue - 2*n
    else:
        startValue = startValue + 2*n 
        
        
        
        code-2
        def pattern(n):
    mid = (n >> 1)
    if n & 1 != 0:
        mid += 1
    val = 1
    for i in range(mid):
        for j in range(val, val + n):
            print(j, end=' ')
        print()
        val += (n << 1)
    if n & 1 != 0:
        val -= (n << 1)
        val -= n
        for i in range(mid, n):
            for j in range(val, val + n):
                print(j, end=' ')
            print()
            val -= (n << 1)
    else:
        val -= n
        for i in range(mid, n):
            for j in range(val, val + n):
                print(j, end=' ')
            print()
            val -= (n << 1)


n = int(input())
pattern(n)
