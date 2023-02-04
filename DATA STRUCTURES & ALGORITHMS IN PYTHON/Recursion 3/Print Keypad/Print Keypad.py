def printKeypadHelper(n, s):
    options = ["", "", "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if (n == 0):
        print(s)
        return

    small = n//10
    lastDigit = n% 10
    ol= len(options[lastDigit])
    if(ol == 0):
        printKeypadHelper(small, s)
        return

    for i in range(0, ol):
        printKeypadHelper(small, options[lastDigit][i] + s)


def printKeypad(n):
    printKeypadHelper(n, "")


n = int(input())
printKeypad(n)
