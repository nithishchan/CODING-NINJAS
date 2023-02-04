def subsequences(string):
    #Implement Your Code Here
    if len(string)==0:
        output=[""]
        return output

    smallOutput = subsequences(string[1:])
    output = []

    for s in smallOutput:
        output.append(s)
        output.append(string[0]+s)
    return output

    pass


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)





