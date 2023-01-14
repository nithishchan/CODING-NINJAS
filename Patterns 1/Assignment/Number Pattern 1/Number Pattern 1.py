Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
111
1111
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
111
1111
11111


n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(1,end="")
    print("")
