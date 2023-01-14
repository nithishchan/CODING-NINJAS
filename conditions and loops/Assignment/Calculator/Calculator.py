Write a program that performs the tasks of a simple calculator.
The program should first take an integer as input and then based on that integer perform the task as given below.
Note: Each answer in next line.
Input format:
Take integers as input, in accordance to the description of the question. 
Constraints:
Time Limit: 1 second
Output format:
The output lines must be as prescribed in the description of the question.
Sample Input:
3
1
2
4
4
2
1
3
2
7
6
Sample Output:
2
2
5
Invalid Operation

# Write your code here
while True:
    i = int(input())
    if(i == 1):
        a = int(input())
        b = int(input())
        c = a+b
        print(c)
    elif(i == 2):
        a = int(input())
        b = int(input())
        c = a-b
        print(c)
    elif(i == 3):
        a = int(input())
        b = int(input())
        c = a*b
        print(c)
    elif(i == 4):
        a = int(input())
        b = int(input())
        c = a/b
        print(int(c))
    elif(i == 5):
        a = int(input())
        b = int(input())
        c = a//b
        print(int(c))
    elif(i == 6):
        quit()
    else:
        print("Invalid Operation")
