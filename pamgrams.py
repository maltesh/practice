
#s = raw_input().strip()
s = 'We promptly judged antique ivory buckles for the next prize'
s = 'We prompt2ly judged antique ivory buckles for the prize'
if s:
    temp = []
    for word in s.split( ' ' ):
        temp.extend(list(word))
    sss = list({( i.upper() ,i.lower()) for i in temp if  ( ord(i) >=65 and ord(i) <=90 ) or ( ord(i)>=97 and ord(i) <=122  )})
    d = {}
    for mm in sss:
        d[ mm[0] ] =mm[1]

    if not sss:
        print 'not pangram'
    if len(sss) ==26:
        print 'pangram'
    else:
        print  'not pangram'
