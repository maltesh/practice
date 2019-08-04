s = str(raw_input())
i = 0
while  len(str(sum(map(int,list(s))))) > 1 or int(s)>9 :
    s = str( sum(map(int,list(str(s)))))
    # print s, '--' ,    str(sum(map(int,list(s)))),  len(str(sum(map(int,list(s)))))
    i = i+1
print i