Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false






def ispalindrome(str):
    if len(str)<=1:
        return True
    if str[0]!=str[len(str)-1]:
        return False
    return ispalindrome(str[1:-1])

str=input()
if ispalindrome(str):
    print("true")
else:
    print("false")

