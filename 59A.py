st = raw_input()
up,low = 0,0
for cr in st:
    if cr.isupper():
        up = up+1
    else:
        low = low +1

if up == low:
    print (st.lower())
elif up>low:
    print (st.upper())
else:
    print (st.lower())
