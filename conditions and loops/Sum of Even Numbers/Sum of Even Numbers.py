Given a number N, print sum of all even numbers from 1 to N.
Input Format :
Integer N
Output Format :
Required Sum 
Sample Input 1 :
 6
Sample Output 1 :
12


n=int(input())
count=1
s=0
while count<=n:
    if (count%2==0):
        s=s+count
    count=count+1
print(s)
