#s = raw_input().strip()
s='SOSOOSOSOSOSOSSOSOSOSOSOSOS'
const_str = 'SOS'
test = [fl == sl for fl,sl in zip(s,'SOS'*100)]
print test.count(False)
