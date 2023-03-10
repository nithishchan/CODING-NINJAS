For a given expression in the form of a string, find if there exist any redundant brackets or not. It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.
Example:
Expression: (a+b)+c
Since there are no needless brackets, hence, the output must be 'false'.

Expression: ((a+b))
The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.
Note:
You will not get a partial score for this problem. You will get marks only if all the test cases are passed.
Input Format :
The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
The first and the only line of output will print either 'true' or 'false'(without the quotes) denoting whether the input expression contains redundant brackets or not.
Note:
You are not required to print the expected result. It has already been taken care of.
Constraints:
0 <= N <= 10^6
Where N is the length of the expression.

Time Limit: 1 second
Sample Input 1:
a+(b)+c 
Sample Output 1:
true
Explanation:
The expression can be reduced to a+b+c. Hence, the brackets are redundant.
Sample Input 2:
(a+b)
Sample Output 2:
false




import queue

def checkRedundant(string):
    if string[0]=='(' and string[2]==')':
        return True
    q=queue.LifoQueue()
    temp=0
    l=len(string)
    for i in range(l-1):
        c=string[i]
        n=string[i+1]
        if c=='(' and n==')':
            return True
        elif c=='(' and n=='(':
            temp=2
        elif c==')' and n==')' and temp==2:
            return True
    return False
    

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')
