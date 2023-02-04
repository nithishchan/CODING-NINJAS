def printsub(s,p):
    if len(s)==0:
        print(p)
        return 

    printsub(s[1:], p)
    printsub(s[1:], p+s[0])

#main
s = input().strip()
printsub(s, '')
