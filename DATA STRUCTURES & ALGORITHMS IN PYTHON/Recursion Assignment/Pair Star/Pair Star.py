Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a







def re(s):
    n = len(s)
    if n <= 1:
        return s
    temp = re(s[1:])
    if s[0] == s[1]:
        return s[0]+"*"+temp
    else:
        return s[0]+temp


s = input().strip()
print(re(s))
