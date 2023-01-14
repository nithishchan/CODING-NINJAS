Print the following pattern for the given number of rows.
Note: N is always odd.
Pattern for N = 5
The dots represent spaces.
Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *
  
  
  n = int(input())
firstHalf = (n + 1) // 2
secondHalf = n // 2
#First Half
currRow = 1 
while currRow <= firstHalf:
    spaces = 1 
    while spaces <= (firstHalf - currRow) :
        print(" ", end = "")
        spaces += 1
    currCol = 1
    while currCol <= (2 * currRow) - 1 :
        print("*", end = "")
        currCol += 1   
    print()
    currRow += 1
#Second Half 
currRow = secondHalf 
while currRow >= 1 :
    spaces = 1
    while spaces <= (secondHalf - currRow + 1) :
        print(" ", end = "") 
        spaces += 1
    currCol = 1 
    while currCol <= (2 * currRow) - 1 :
        print("*", end = "") 
        currCol += 1
    print()
    currRow -=1
    
    
    
    code-2
    def display(n):
    sp = n // 2
    st = 1
    for i in range(1, n + 1):
        for j in range(1, sp + 1):
            print(" ", end='')
        count = st // 2 + 1
        for k in range(1, st + 1):
            print("*", end='')
            if (k <= (st // 2)):
                count -= 1
            else:
                count += 1

        print()
        
        if (i <= n // 2):
            sp -= 1
            st += 2
        else:
            sp += 1
            st -= 2


n = int(input())
display(n)
