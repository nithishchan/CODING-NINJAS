Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
Input format :
Numeric string S (string, Eg. "1234")
Output format :
Corresponding integer N (int, Eg. 1234)
Constraints :
0 < |S| <= 9
where |S| represents length of string S.
Sample Input 1 :
00001231
Sample Output 1 :
1231
Sample Input 2 :
12567
Sample Output 2 :
12567




def s_to_i(string, num):
    if len(string) == 0:
        return num

    return s_to_i(string[1:], num*10 + ord(string[0])-48)


string = input()
num = 0
print(s_to_i(string, num))
