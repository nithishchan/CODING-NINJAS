Print the following pattern for the given N number of rows.
Pattern for N = 4




The dots represent spaces.


Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
3
Sample Output 1:
      1 
    12
  123
Sample Input 2:
4
Sample Output 2:
      1 
    12
  123
1234

num=int(input())
i=1
while i<=num:
    spaces=1
    while spaces <=num-i:
        print(" ",end="")
        spaces=spaces+1
    stars=1
    while stars<=i:
        print(stars,end="")
        stars=stars+1
    print()
    i=i+1
