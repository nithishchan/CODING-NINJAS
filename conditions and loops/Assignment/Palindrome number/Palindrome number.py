Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
Sample Input 1 :
121
Sample Output 1 :
true
Sample Input 2 :
1032
Sample Output 2 :
false


def checkPalindrome(num):
    n = num
    rn = 0    
    while(n > 0):    
       r = n %10    
       rn = (rn *10) + r    
       n = n //10    
    if rn == num:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
