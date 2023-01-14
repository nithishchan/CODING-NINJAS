Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******
 
 
 num=int(input())
i=1

while i<=num:
    j = 0
    while j<num-i:
        print(" ",end="")
        j=j+1
    k=0
    while k<i:
        print("*",end="")
        k=k+1
    k=1
    while k<i:
        print("*",end="")
        k=k+1
    i=i+1
    print()
