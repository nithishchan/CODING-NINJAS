options=[ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" ]
def keypad(n):
    #Implement Your Code Here
    if n==0:
        output=[""]
        return output
    smallNumber= keypad(n//10)
    lastDigit = options[n % 10]
    output=[]

    for c  in lastDigit:
        for s in smallNumber:
            output.append(s+c)
    return output
  
    pass

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
