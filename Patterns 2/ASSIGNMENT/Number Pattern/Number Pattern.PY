Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5


CODE-1

a=int(input())

for k in range(1,a+1):
    b='1'
    for i in range(2,a+1):
        c=str(i)
        if k >= i:
            b=b+c
        else:
            b=b+' '
    for j in range(a,0,-1):
        d=str(j)
        if k >= j:
            b=b+d
        else:
            b=b+' '
    print(b)
    
    CODE-2
    
num = int(input())
i = 1
while num >= i:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1

    space = 1
    spaces = 1
    while spaces <= (num-i):
        print(" ", end="")
        spaces = spaces+1
    spaces = 1
    while spaces <= (num-i):
        print(" ", end="")
        spaces = spaces+1
    k = i
    while k >= 1:
        print(k, end="")
        k = k-1
    print()
    i += 1
