Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
      212
    32123
  4321234
543212345

n = int(input())
i = 1

while i <= n:
    sp = 1
    while sp <= n-i:
        print(' ',end ='')
        sp = sp + 1
        
    p = i
    j = 1
    
    while j <= i:
        print(p, end ='')
        p = p - 1
        j = j + 1
        
    p = 2
    while p <= i:
        print(p, end ='')
        p = p + 1
    
    print()
    i = i + 1
    
    code -2
    
    row = int(input())

for i in range(1, row+1):

    for j in range(1, row+1-i):
        print(' ', end='')

    for j in range(i, 0, -1):
        print(j, end='')

    for j in range(2, i+1):
        print(j, end='')

    print()
