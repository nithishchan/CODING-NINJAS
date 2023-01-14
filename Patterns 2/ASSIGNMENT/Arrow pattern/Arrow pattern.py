Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*

n=int(input())
increasing=(n+1)//2
decreasing=n-increasing
i=1
while i<=increasing:
    s=1
    while s<=i-1:
        print('*',end="")
        s=s+1
    j=1
    while j<=i:
        print('',end="")
        j=j+1
    print()
    i=i+1
i=1
while i<=decreasing:
    s=1
    while s<=decreasing-i:
        s=1
        while s<=i-1:
            print('',end="")
            s=s+1
        j=1
        while j<=decreasing-i+1:
            print('*',end="")
            j=j+1
        print()
        i=i+1
        
        
        code-2
        
        
num = int(input())
for i in range(1, num+1):
    if i <= round(num/2):
        for j in range(1, i):
            print(" ", end="")
        for j in range(0, i):
            print("*", end=" ")
    else:
        for j in range(1, num-i+1):
            print(" ", end="")
        for j in range(0, num-i+1):
            print("*", end=" ")
    print()
