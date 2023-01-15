Given a string, compute recursively a new string where all 'x' chars have been removed.
Input format :
String S
Output format :
Modified String
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string S. 
Sample Input 1 :
xaxb
Sample Output 1:
ab
Sample Input 2 :
abc
Sample Output 2:
abc



# Problem: Remove x from string

def removeX(s):
    chr = 'x'
    l = len(s)
    if len(s) == 0:
        return s
    smalleroutput = removeX(s[1:])
    if s[0] == chr:
        return ''+smalleroutput
    else:
        return s[0]+smalleroutput


string = input()
print(removeX(string))
