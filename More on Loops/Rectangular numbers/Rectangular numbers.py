Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333

n = int(input())
for i in range(1,n+1):
    temp = n
    for j in range(1,i):
        print(temp,end="")
        temp = temp -1
    for j in range(1,(2*n) - (2*i) + 2):
        print(n-i+1,end="")
    for j in range(1,i):
        temp = temp+1
        print(temp,end="")
    print()
for i in range(n-1,0,-1):
    temp = n
    for j in range(1,i):
        print(temp,end="")
        temp = temp - 1 
    for j in range(1,(2*n) - (2*i) + 2):
        print(n-i+1,end="")
    for j in range(1,i):
        temp = temp+1
        print(temp,end="")
    print()
    
    code-2
    
    def prints(a, size):
    for i in range(size):
        for j in range(size):
            print(a[i][j], end='')
        print()


def innerPattern(n):

    size = 2 * n - 1
    front = 0
    back = size - 1
    a = [[0 for i in range(MAX)]
         for i in range(MAX)]
    while (n != 0):
        for i in range(front, back + 1):
            for j in range(front, back + 1):
                if (i == front or i == back or
                        j == front or j == back):
                    a[i][j] = n
        front += 1
        back -= 1
        n -= 1
    prints(a, size)


n = int(input())
innerPattern(n)
